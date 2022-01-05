from kata2 import *

def test_remove_space(): 
    character_name= '     super man   ' 
    result = remove_space(character_name)
    expected = 'super-man'

    assert result == expected

def test_capitalize_title(): 
    title = "a pequena sereia"
    result = capitalize_title(title)
    expected = "A Pequena Sereia"
    assert result == expected 


def test_capitalize_text(): 
    text = """a América Latina está longe de retornar aos níveis de expansão pré-pandêmica, que já eram baixos em 2019. globalmente, 40% da população mais pobre ainda não começou a recuperar sua renda perdida devido à pandemia. mais de 100 milhões de pessoas caíram na pobreza extrema devido ao covid-19, de acordo com o Banco Mundial."""
    result = capitalize_text(text)
    expected = """A América Latina está longe de retornar aos níveis de expansão pré-pandêmica, que já eram baixos em 2019. Globalmente, 40% da população mais pobre ainda não começou a recuperar sua renda perdida devido à pandemia. Mais de 100 milhões de pessoas caíram na pobreza extrema devido ao covid-19, de acordo com o Banco Mundial."""
    assert result == expected


def test_title_creator(): 
    text = "pense em um deserto"
    result = title_creator(text) 
    expect = "--------------------Pense Em Um Deserto--------------------"
    assert result == expect

def test_text_creator(): 
    text_one = """ o disco “30” é agora     o projeto lançado      em 2021 com mais tempo     em primeiro lugar na parada, superando "Sour"             , de Olivia Rodrigo. além disso,  Adele conquistou o título de artista solo britânica com o maior tempo no topo da Billboard 200              na história      ao completar 40    semanas em número 1. """
    text_two = """ Já Olivia Rodrigo não tem do que reclamar. seu    disco –     atualmente na quarta posição – continua    com  o recorde de álbum com    mais tempo no Top 10    da parada nesta década, com 31    semanas."""

    result = text_creator(text_one, text_two)
    
    expected = """O disco “30” é agora o projeto lançado em 2021 com mais tempo em primeiro lugar na parada, superando "Sour", de Olivia Rodrigo. Além disso, Adele conquistou o título de artista solo britânica com o maior tempo no topo da Billboard 200 na história ao completar 40 semanas em número 1 já Olivia Rodrigo não tem do que reclamar. Seu disco – atualmente na quarta posição – continua com o recorde de álbum com mais tempo no Top 10 da parada nesta década, com 31 semanas"""
    
    assert result == expected 