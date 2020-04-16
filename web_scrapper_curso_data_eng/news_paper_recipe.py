import argparse
import logging
import ntpath
from urllib.parse import urlparse

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

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('filename',
                      help='The path to the dirty data',
                      type=str)

  args = parser.parse_args()

  df = main(args.filename)

  print(df)
  print(df['title'].isna())
