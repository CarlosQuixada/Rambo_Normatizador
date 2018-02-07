# -*- coding: utf-8 -*-
from __future__ import print_function
import nltk
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class Analise (object):
    def __init__(self):

        self.dataPath_treino = 'normatizador/classificacao/treino.csv'
        self.stopwordsnltk = nltk.corpus.stopwords.words('portuguese')

        self.base = self.getBase()
        self.treino = self.aplicastemmer(self.base)
        self.palavrastreinamento = self.buscapalvras(self.treino)
        self.frequenciatreinamento = self.buscafrequencia(self.palavrastreinamento)
        self.palavrasunicastreinamento = self.buscapalavrasunicas(self.frequenciatreinamento)

    def getBase(self):
        dados = []

        with open(self.dataPath_treino, 'rb') as file:
            reader = csv.reader(file)

            for row in reader:
                print(row)
                dados.append((row[0],row[1]))
        return dados

    def aplicastemmer(self,texto):
        stemmer = nltk.stem.RSLPStemmer()
        frasesstemming =[]
        for (palavras,emocao) in texto:
            comstemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in self.stopwordsnltk]
            frasesstemming.append((comstemming,emocao))
        return frasesstemming

    def buscapalvras(self,frases):
        todaspalvras=[]
        for (palavras,emocao) in frases:
            todaspalvras.extend(palavras)
        return todaspalvras

    def buscafrequencia(self,palavras):
        palavras = nltk.FreqDist(palavras)
        return palavras

    def buscapalavrasunicas(self,frequencia):
        freq = frequencia.keys()
        return freq

    def extratorpalavrasTreino(self,documento):
        doc = set(documento)
        caracteristicas = {}

        for palavras in self.palavrasunicastreinamento:
            caracteristicas['%s' %palavras] = (palavras in doc)
        return caracteristicas

    def treinar(self):
        basecompletaTreino = nltk.classify.apply_features(self.extratorpalavrasTreino, self.treino)
        classificador = nltk.NaiveBayesClassifier.train(basecompletaTreino)
        print(classificador.labels())
        return classificador

    def classificarProduto(self,classificador,produto):
        topicostemming = []
        stemmer = nltk.stem.RSLPStemmer()

        for (palavrastreinamento) in produto.split():
            comstem = [p for p in palavrastreinamento.split()]
            topicostemming.append(str(stemmer.stem(comstem[0])))

        novoProduto = self.extratorpalavrasTreino(topicostemming)
        return classificador.classify(novoProduto)

    def classificar(self, produto):
        classificador = self.treinar()
        produtoClassificado = self.classificarProduto(classificador,produto)
        print(produtoClassificado)
        return produtoClassificado