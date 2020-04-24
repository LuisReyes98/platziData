import argparse
import logging
import ntpath
from urllib.parse import urlparse
import hashlib

"""
nltk es una libreria enorme que se basa en la lectura de
lenguage natural
la primera vez que se ejecuta se debaran descargar los modulos necesarios
"""
import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words('spanish'))

import pandas as pd

logging.basicConfig(level= logging.INFO)

logger = logging.getLogger(__name__)


def main(filename):
  """Main de la funcion"""

  logger.info('Starting cleaning process')

  df = _read_data(filename)

  newspaper_uid = _extract_newspaper_uid(filename)

  df = _add_newspaper_uid_column(df, newspaper_uid)
  df = _extract_host(df)
  df = _fill_missing_title(df)
  df = _generate_uids_for_rows(df)
  df = _remove_new_lines_from_body(df)
  df = _tokenize_column(df, 'title')
  df = _tokenize_column(df, 'body')
  df = _remove_duplicates_entries(df, 'title')
  df = _drop_rows_with_missing_values(df)

  _save_data(df,filename)

  return df

def _read_data(filename):
  """"""
  logger.info('Reading file {}'.format(filename))

  return pd.read_csv(filename)

def _extract_newspaper_uid(filename):
  """ Se limpia el path dado y del nombre del archivo
  en base al formato seguido se obtiene el path"""
  logger.info('Extracting newspaper uid')

  cleaned_filename = ntpath.split(filename)[1]

  newspaper_uid = cleaned_filename.split('_')[0]

  logger.info('Newspaper uid detected: {}'.format(newspaper_uid))

  return newspaper_uid

def _add_newspaper_uid_column(df, newspaper_uid):
  """ se agrega el uid del newspaper"""
  logger.info('Filling news_paper_uid column with {}'.format(newspaper_uid))

  df['newspaper_uid'] = newspaper_uid

  return df


def _extract_host(df):
  """"""
  logger.info('Extracting host from urls')

  df['host'] = df['url'].apply(lambda url: urlparse(url).netloc)

  return df


def _fill_missing_title(df):
  logger.info('Filling missing titles')

  missing_titles_mask = df['title'].isna()

  missing_titles = (df[missing_titles_mask]['url']
                      .str.extract(r'(?P<missing_titles>[^/]+)$')
                      .applymap(lambda title: title.split('-'))
                      .applymap(lambda title_word_list: ' '.join(title_word_list))
                    )
  df.loc[missing_titles_mask, 'title'] = missing_titles.loc[:, 'missing_titles']

  return df


def _generate_uids_for_rows(df):
  """ Se generan los uids en base al url """
  logger.info('Generating uids for each row')

  uids = (df
          .apply(lambda row: hashlib.md5(bytes(row['url'].encode())), axis=1)
          .apply(lambda hash_object: hash_object.hexdigest())
          )

  df['uid'] = uids

  return df.set_index('uid')


def _remove_new_lines_from_body(df):
  logger.info('Remove new lines from body')

  stripped_body = (df
                    .apply(lambda row: row['body'], axis=1)
                    .apply(lambda body: list(body))
                    .apply(lambda letters: list(map(lambda letter: letter.replace('\n',' '), letters)))
                    .apply(lambda letters: ''.join(letters))
                  )
  df['body'] = stripped_body

  return df


def _tokenize_column(df, column_name):
  """
    _tokenize_column(df, column_name, new_column_name) -> Dataframe
    Keyword arguments:
    df -- Dataframe
    column_name -- String, name of the column to tokenize
    new_column_name -- String name of the column that will have the tokenized results
  """
  tokenize_column = (df
          .dropna()
          .apply(lambda row: nltk.word_tokenize(row[column_name]), axis=1)
          .apply(lambda tokens: list(filter(lambda token: token.isalpha(), tokens)))
          .apply(lambda tokens: list(map(lambda token: token.lower(), tokens)))
          .apply(lambda word_list: list(filter(lambda word: word not in stop_words, word_list)))
          .apply(lambda valid_word_list: len(valid_word_list))
          )

  df['n_tokens_'+column_name] = tokenize_column

  return df


def _remove_duplicates_entries(df, column_name):
  logger.info('Removing duplicate entries')

  df.drop_duplicates(subset=[column_name], keep='first', inplace=True)

  return df


def _drop_rows_with_missing_values(df):
  logger.info('Dropping rows with missing values')

  return df.dropna()


def _save_data(df,filename):
  """
    Guardar un dataframe como .csv con el filename dado
  """
  file_path, cleaned_filename = ntpath.split(filename)

  cleaned_filename = 'clean_{}'.format(cleaned_filename)
  result_path = '{path}/{file_name}'.format(path=file_path, file_name=cleaned_filename)
  logger.info('Saving data at location: {}'.format(
      result_path))

  df.to_csv(result_path)


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('filename',
                      help='The path to the dirty data',
                      type=str)

  args = parser.parse_args()

  df = main(args.filename)

  print(df)
