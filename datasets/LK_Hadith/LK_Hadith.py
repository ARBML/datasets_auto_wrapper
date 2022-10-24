import os
import pandas as pd 
import datasets

class LK_Hadith(datasets.GeneratorBasedBuilder):
	def _info(self):
		return datasets.DatasetInfo(features=datasets.Features({'Chapter_Number':datasets.Value('string'),'Chapter_English':datasets.Value('string'),'Chapter_Arabic':datasets.Value('string'),'Section_Number':datasets.Value('string'),'Section_English':datasets.Value('string'),'Section_Arabic':datasets.Value('string'),'Hadith_number':datasets.Value('string'),'English_Hadith':datasets.Value('string'),'English_Isnad':datasets.Value('string'),'English_Matn':datasets.Value('string'),'Arabic_Hadith':datasets.Value('string'),'Arabic_Isnad':datasets.Value('string'),'Arabic_Matn':datasets.Value('string'),'Arabic_Comment':datasets.Value('string'),'English_Grade':datasets.Value('string'),'Arabic_Grade':datasets.Value('string')}))
	def _split_generators(self, dl_manager):
		url = ['http://github.com/ShathaTm/LK-Hadith-Corpus/archive/master.zip']
		downloaded_files = dl_manager.download_and_extract(url)
		return [datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={'filepaths':[os.path.join(downloaded_files[0],f) for f in ['LK-Hadith-Corpus-master/Tirmizi/Chapter17.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter47.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter3.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter18.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter38.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter23.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter9.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter14.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter41.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter7.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter6.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter28.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter44.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter5.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter42.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter13.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter46.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter36.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter20.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter27.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter32.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter25.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter37.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter49.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter22.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter4.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter15.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter48.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter30.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter10.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter11.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter40.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter19.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter43.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter45.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter21.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter34.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter1.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter35.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter8.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter2.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter12.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter29.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter39.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter16.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter31.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter24.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter26.csv', 'LK-Hadith-Corpus-master/Tirmizi/Chapter33.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter88.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter17.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter47.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter3.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter18.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter87.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter81.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter38.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter23.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter75.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter82.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter94.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter97.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter9.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter14.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter41.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter51.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter84.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter74.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter7.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter6.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter28.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter44.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter67.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter60.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter90.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter85.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter76.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter5.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter58.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter89.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter80.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter78.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter42.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter96.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter13.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter46.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter36.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter20.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter77.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter79.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter27.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter32.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter25.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter37.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter49.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter86.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter57.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter22.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter4.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter15.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter48.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter30.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter10.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter55.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter61.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter91.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter66.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter68.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter71.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter73.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter92.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter11.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter40.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter19.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter43.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter45.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter21.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter34.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter1.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter54.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter35.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter69.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter8.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter2.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter12.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter29.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter62.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter52.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter39.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter65.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter56.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter16.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter31.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter24.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter83.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter26.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter53.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter33.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter64.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter63.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter70.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter50.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter93.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter59.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter72.csv', 'LK-Hadith-Corpus-master/Bukhari/Chapter95.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter17.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter3.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter18.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter23.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter9.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter14.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter7.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter6.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter28.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter0.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter5.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter13.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter36.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter20.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter27.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter32.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter25.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter37.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter22.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter4.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter15.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter30.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter10.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter11.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter19.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter21.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter34.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter1.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter35.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter8.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter2.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter12.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter29.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter16.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter31.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter24.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter26.csv', 'LK-Hadith-Corpus-master/IbnMaja/Chapter33.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter17.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter47.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter3.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter18.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter38.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter23.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter9.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter14.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter41.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter51.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter7.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter6.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter28.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter44.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter5.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter42.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter13.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter46.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter36.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter20.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter27.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter32.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter25.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter37.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter49.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter22.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter4.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter15.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter48.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter30.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter10.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter11.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter40.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter19.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter43.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter45.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter21.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter34.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter1.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter35.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter8.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter2.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter12.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter29.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter39.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter16.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter31.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter24.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter26.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter33.csv', 'LK-Hadith-Corpus-master/Nesai/Chapter50.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter17.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter47.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter3.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter18.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter38.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter23.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter9.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter14.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter41.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter51.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter7.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter6.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter28.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter44.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter0.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter5.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter42.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter13.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter46.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter36.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter20.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter27.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter32.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter25.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter37.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter49.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter22.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter4.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter15.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter48.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter30.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter10.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter55.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter11.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter40.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter19.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter43.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter45.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter21.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter34.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter1.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter54.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter35.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter8.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter2.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter12.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter29.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter52.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter39.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter56.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter16.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter31.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter24.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter26.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter53.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter33.csv', 'LK-Hadith-Corpus-master/Muslim/Chapter50.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter17.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter3.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter18.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter38.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter23.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter9.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter14.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter41.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter7.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter6.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter28.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter5.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter42.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter13.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter36.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter20.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter27.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter32.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter25.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter37.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter22.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter4.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter15.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter30.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter10.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter11.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter40.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter19.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter43.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter21.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter34.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter1.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter35.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter8.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter2.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter12.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter29.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter39.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter16.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter31.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter24.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter26.csv', 'LK-Hadith-Corpus-master/AbuDaud/Chapter33.csv']]})]
	def _generate_examples(self, filepaths):
		_id = 0
		for filepath in filepaths:
			df = pd.read_csv(open(filepath, 'rb'), sep = ',', skiprows = 0, error_bad_lines = False, header = 0)
			df.columns = ['Chapter_Number', 'Chapter_English', 'Chapter_Arabic', 'Section_Number', 'Section_English', 'Section_Arabic', 'Hadith_number', 'English_Hadith', 'English_Isnad', 'English_Matn', 'Arabic_Hadith', 'Arabic_Isnad', 'Arabic_Matn', 'Arabic_Comment', 'English_Grade', 'Arabic_Grade']
			for _, record in df.iterrows():
				yield str(_id), {'Chapter_Number':record['Chapter_Number'],'Chapter_English':record['Chapter_English'],'Chapter_Arabic':record['Chapter_Arabic'],'Section_Number':record['Section_Number'],'Section_English':record['Section_English'],'Section_Arabic':record['Section_Arabic'],'Hadith_number':record['Hadith_number'],'English_Hadith':record['English_Hadith'],'English_Isnad':record['English_Isnad'],'English_Matn':record['English_Matn'],'Arabic_Hadith':record['Arabic_Hadith'],'Arabic_Isnad':record['Arabic_Isnad'],'Arabic_Matn':record['Arabic_Matn'],'Arabic_Comment':record['Arabic_Comment'],'English_Grade':record['English_Grade'],'Arabic_Grade':record['Arabic_Grade']}
				_id += 1 

