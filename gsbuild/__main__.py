import urllib.request as urlrequest
import fontTools.ttLib.woff2 as woff2
import argparse
import tempfile
import os
import shutil


def webfont(style, alphabet):

    class MetaData:
        def __init__(self, url, filename):
            url = self.url
            filename = self.filename

    thin_italic = {'url': {
        'cyrillic': 'https://fonts.gstatic.com/s/productsans/v12/pxifypQkot1TnFhsFMOfGShVEu_vWEpkr1ap.woff2',
        'greek': 'https://fonts.gstatic.com/s/productsans/v12/pxifypQkot1TnFhsFMOfGShVEu_vWE1kr1ap.woff2',
        'latin-ext': 'https://fonts.gstatic.com/s/productsans/v12/pxifypQkot1TnFhsFMOfGShVEu_vWEBkr1ap.woff2',
        'latin': 'https://fonts.gstatic.com/s/productsans/v12/pxifypQkot1TnFhsFMOfGShVEu_vWE5krw.woff2'},
        'filename': 'ProductSans-ThinItalic'}
    light_italic = {'url': {
        'cyrillic': 'https://fonts.gstatic.com/s/productsans/v12/pxieypQkot1TnFhsFMOfGShVEu8nSllHimuQpw.woff2',
        'greek': 'https://fonts.gstatic.com/s/productsans/v12/pxieypQkot1TnFhsFMOfGShVEu8nSllAimuQpw.woff2',
        'latin-ext': 'https://fonts.gstatic.com/s/productsans/v12/pxieypQkot1TnFhsFMOfGShVEu8nSllNimuQpw.woff2',
        'latin': 'https://fonts.gstatic.com/s/productsans/v12/pxieypQkot1TnFhsFMOfGShVEu8nSllDims.woff2'},
        'filename': 'ProductSans-LightItalic'}
    italic = {'url': {
        'cyrillic': 'https://fonts.gstatic.com/s/productsans/v12/pxidypQkot1TnFhsFMOfGShVEueIaEx8qw.woff2',
        'greek': 'https://fonts.gstatic.com/s/productsans/v12/pxidypQkot1TnFhsFMOfGShVEuePaEx8qw.woff2',
        'latin-ext': 'https://fonts.gstatic.com/s/productsans/v12/pxidypQkot1TnFhsFMOfGShVEueCaEx8qw.woff2',
        'latin': 'https://fonts.gstatic.com/s/productsans/v12/pxidypQkot1TnFhsFMOfGShVEueMaEw.woff2'},
        'filename': 'ProductSans-Italic'}
    medium_italic = {'url': {
        'cyrillic': 'https://fonts.gstatic.com/s/productsans/v12/pxieypQkot1TnFhsFMOfGShVEu9_S1lHimuQpw.woff2',
        'greek': 'https://fonts.gstatic.com/s/productsans/v12/pxieypQkot1TnFhsFMOfGShVEu9_S1lAimuQpw.woff2',
        'latin-ext': 'https://fonts.gstatic.com/s/productsans/v12/pxieypQkot1TnFhsFMOfGShVEu9_S1lNimuQpw.woff2',
        'latin': 'https://fonts.gstatic.com/s/productsans/v12/pxieypQkot1TnFhsFMOfGShVEu9_S1lDims.woff2'},
        'filename': 'ProductSans-MediumItalic'}
    bold_italic = {'url': {
        'cyrillic': 'https://fonts.gstatic.com/s/productsans/v12/pxieypQkot1TnFhsFMOfGShVEu83TVlHimuQpw.woff2',
        'greek': 'https://fonts.gstatic.com/s/productsans/v12/pxieypQkot1TnFhsFMOfGShVEu83TVlAimuQpw.woff2',
        'latin-ext': 'https://fonts.gstatic.com/s/productsans/v12/pxieypQkot1TnFhsFMOfGShVEu83TVlNimuQpw.woff2',
        'latin': 'https://fonts.gstatic.com/s/productsans/v12/pxieypQkot1TnFhsFMOfGShVEu83TVlDims.woff2'},
        'filename': 'ProductSans-BoldItalic'}
    black_italic = {'url': {
        'cyrillic': 'https://fonts.gstatic.com/s/productsans/v12/pxieypQkot1TnFhsFMOfGShVEu8PT1lHimuQpw.woff2',
        'greek': 'https://fonts.gstatic.com/s/productsans/v12/pxieypQkot1TnFhsFMOfGShVEu8PT1lAimuQpw.woff2',
        'latin-ext': 'https://fonts.gstatic.com/s/productsans/v12/pxieypQkot1TnFhsFMOfGShVEu8PT1lNimuQpw.woff2',
        'latin': 'https://fonts.gstatic.com/s/productsans/v12/pxieypQkot1TnFhsFMOfGShVEu8PT1lDims.woff2'},
        'filename': 'ProductSans-BlackItalic'}
    thin = {'url': {
        'cyrillic': 'https://fonts.gstatic.com/s/productsans/v12/pxidypQkot1TnFhsFMOfGShddOeIaEx8qw.woff2',
        'greek': 'https://fonts.gstatic.com/s/productsans/v12/pxidypQkot1TnFhsFMOfGShddOePaEx8qw.woff2',
        'latin-ext': 'https://fonts.gstatic.com/s/productsans/v12/pxidypQkot1TnFhsFMOfGShddOeCaEx8qw.woff2',
        'latin': 'https://fonts.gstatic.com/s/productsans/v12/pxidypQkot1TnFhsFMOfGShddOeMaEw.woff2'},
        'filename': 'ProductSans-Thin'}
    light = {'url': {
        'cyrillic': 'https://fonts.gstatic.com/s/productsans/v12/pxicypQkot1TnFhsFMOfGShdvPWbS2lBkm8.woff2',
        'greek': 'https://fonts.gstatic.com/s/productsans/v12/pxicypQkot1TnFhsFMOfGShdvPWbTGlBkm8.woff2',
        'latin-ext': 'https://fonts.gstatic.com/s/productsans/v12/pxicypQkot1TnFhsFMOfGShdvPWbQWlBkm8.woff2',
        'latin': 'https://fonts.gstatic.com/s/productsans/v12/pxicypQkot1TnFhsFMOfGShdvPWbT2lB.woff2'},
        'filename': 'ProductSans-Light'}
    regular = {'url': {
        'cyrillic': 'https://fonts.gstatic.com/s/productsans/v12/pxiDypQkot1TnFhsFMOfGShVE9eOcEg.woff2',
        'greek': 'https://fonts.gstatic.com/s/productsans/v12/pxiDypQkot1TnFhsFMOfGShVFNeOcEg.woff2',
        'latin-ext': 'https://fonts.gstatic.com/s/productsans/v12/pxiDypQkot1TnFhsFMOfGShVGdeOcEg.woff2',
        'latin': 'https://fonts.gstatic.com/s/productsans/v12/pxiDypQkot1TnFhsFMOfGShVF9eO.woff2'},
        'filename': 'ProductSans-Regular'}
    medium = {'url': {
        'cyrillic': 'https://fonts.gstatic.com/s/productsans/v12/pxicypQkot1TnFhsFMOfGShd5PSbS2lBkm8.woff2',
        'greek': 'https://fonts.gstatic.com/s/productsans/v12/pxicypQkot1TnFhsFMOfGShd5PSbTGlBkm8.woff2',
        'latin-ext': 'https://fonts.gstatic.com/s/productsans/v12/pxicypQkot1TnFhsFMOfGShd5PSbQWlBkm8.woff2',
        'latin': 'https://fonts.gstatic.com/s/productsans/v12/pxicypQkot1TnFhsFMOfGShd5PSbT2lB.woff2'},
        'filename': 'ProductSans-Medium'}
    bold = {'url': {
        'cyrillic': 'https://fonts.gstatic.com/s/productsans/v12/pxicypQkot1TnFhsFMOfGShdrPKbS2lBkm8.woff2',
        'greek': 'https://fonts.gstatic.com/s/productsans/v12/pxicypQkot1TnFhsFMOfGShdrPKbTGlBkm8.woff2',
        'latin-ext': 'https://fonts.gstatic.com/s/productsans/v12/pxicypQkot1TnFhsFMOfGShdrPKbQWlBkm8.woff2',
        'latin': 'https://fonts.gstatic.com/s/productsans/v12/pxicypQkot1TnFhsFMOfGShdrPKbT2lB.woff2'},
        'filename': 'ProductSans-Bold'}
    black = {'url': {
        'cyrillic': 'https://fonts.gstatic.com/s/productsans/v12/pxicypQkot1TnFhsFMOfGShdlPCbS2lBkm8.woff2',
        'greek': 'https://fonts.gstatic.com/s/productsans/v12/pxicypQkot1TnFhsFMOfGShdlPCbTGlBkm8.woff2',
        'latin-ext': 'https://fonts.gstatic.com/s/productsans/v12/pxicypQkot1TnFhsFMOfGShdlPCbQWlBkm8.woff2',
        'latin': 'https://fonts.gstatic.com/s/productsans/v12/pxicypQkot1TnFhsFMOfGShdlPCbT2lB.woff2'},
        'filename': 'ProductSans-Black'}

    alias = {'thin_italic': thin_italic,
             'light_italic': light_italic,
             'italic': italic,
             'medium_italic': medium_italic,
             'bold_italic': bold_italic,
             'black_italic': black_italic,
             'thin': thin,
             'light': light,
             'regular': regular,
             'medium': medium,
             'bold': bold,
             'black': black}

    style = alias[style]

    product_sans = MetaData
    product_sans.url = style['url'][alphabet]
    product_sans.filename = style['filename']
    return product_sans


if __name__ == '__main__':

    argument_parser = argparse.ArgumentParser(description='Builds an installable TTF file of Google\'s Product Sans')
    argument_parser.add_argument('alphabet',
                                 metavar='alphabet',
                                 type=str,
                                 help='specifies which alphabet you want to build the font for')
    arguments = argument_parser.parse_args()

    if arguments.alphabet not in ['cyrillic', 'greek', 'latin-ext', 'latin']:
        print('Invalid alphabet, please retry')
        exit()

    print('GSBuild by Muda42')

    starting_dir = os.getcwd()
    temp_dir = tempfile.mkdtemp()
    install_dir = starting_dir + '\\Google Sans\\' + arguments.alphabet

    styles = {'thin_italic',
              'light_italic',
              'italic',
              'medium_italic',
              'bold_italic',
              'black_italic',
              'thin',
              'light',
              'regular',
              'medium',
              'bold',
              'black'}

    if os.path.exists(install_dir):
        shutil.rmtree(install_dir)
    os.makedirs(install_dir)
    os.chdir(temp_dir)
    print('Downloading webfonts from Google\'s API')
    for element in styles:
        font = webfont(element, arguments.alphabet)
        try:
            urlrequest.urlretrieve(font.url, font.filename)
        except:
            print('Failed to download webfont')
            os.chdir(starting_dir)
            shutil.rmtree(temp_dir)
            shutil.rmtree(install_dir)
            exit()
        print('Converting ' + font.filename + ' to ttFont        ', end='\r')
        ttf_font = font.filename + '.ttf'
        woff2.decompress(font.filename, ttf_font)
        shutil.move(ttf_font, install_dir + '\\' + ttf_font)

    print('ttFont files have been created at ' + os.path.realpath(install_dir))

    os.chdir(starting_dir)
    shutil.rmtree(temp_dir)
