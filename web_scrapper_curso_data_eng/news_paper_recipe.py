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

  df = _tokenize_column(df, 'title', 'n_tokens_title')
  df = _tokenize_column(df, 'body', 'n_tokens_body')

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


def _tokenize_column(df, column_name, new_column_name):
  tokenize_column = (df
          .dropna()
          .apply(lambda row: nltk.word_tokenize(row[column_name]), axis=1)
          .apply(lambda tokens: list(filter(lambda token: token.isalpha(), tokens)))
          .apply(lambda tokens: list(map(lambda token: token.lower(), tokens)))
          .apply(lambda word_list: list(filter(lambda word: word not in stop_words, word_list)))
          .apply(lambda valid_word_list: len(valid_word_list))
          )

  df[new_column_name] = tokenize_column

  return df

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('filename',
                      help='The path to the dirty data',
                      type=str)

  args = parser.parse_args()

  df = main(args.filename)

  print(df)
