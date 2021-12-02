%query1
estafeta(alexandre, [encomenda(camisola, 2, 15, bicicleta, 10, rua(capa, gualtar), ana, tempo(2021,10,15,21), 4), 
                 encomenda(meias, 1, 1, bicicleta, 5, rua(vicente, gualtar), armando, tempo(2021,11,3,17), 3), 
                 encomenda(camisola, 2, 10, bicicleta, 7, rua(bouca, gualtar), antonio, tempo(2021,9,23,10), 5)]).


estafeta(bernardo, [encomenda(boia, 10, 20, mota, 12, rua(sol, gualtar), beatriz, tempo(2021,11,8,19), 3),
                  encomenda(bracadeiras, 5, 6, mota, 4, rua(fonte, gualtar), barbara, tempo(2021,10,21,3), 5),
                  encomenda(prancha, 15, 2, mota, 24, rua(capa, gualtar), bernardina, tempo(2021,9,20,6), 2)]).


estafeta(carlos, [encomenda(rosas, 50, 100, carro, 12, rua(quintao, adaufe), camila, tempo(2021,11,12,10), 3),
                   encomenda(carvalhos, 40, 200, carro, 18, rua(colonias, burgaes), casemiro, tempo(2021,9,31,21), 2),
                   encomenda(eucaliptos, 50, 450, carro, 22, rua(paco, espinho), costa, tempo(2021,10,20,4), 1)]).

estafeta(duarte, [encomenda(espátula, 1, 5, bicicleta, 5, rua(lameiros, espinho), dinis, tempo(2021,10,2,14), 5),
                   encomenda(microondas, 15, 100, mota, 12, rua(capa, gualtar), daniela, tempo(2021,9,6,17), 2),
                   encomenda(frigorifico, 90, 250, carro, 19, rua(padassas, burgaes), diogo, tempo(2021,11,10,16), 1)]).

estafeta(eduardo, [encomenda(farol, 2, 20, bicicleta, 3, rua(presa, arcozelo), emilia, tempo(2021,10,3,1), 3)]).

%query3

estafeta(fernando, [encomenda(sapatos, 2, 2, bicicleta, 5, rua(vicente, gualtar), francisco, tempo(2021,11,2,18), 5)]).

estafeta(goncalo, [encomenda(camisola, 5, 15, bicicleta, 12, rua(capa, gualtar), guilherme, tempo(2021,9,10,15), 4),
                        encomenda(calcas, 4, 10, bicicleta, 12, rua(padassas, burgaes), gabriel, tempo(2021,11,17,20), 3),
                        encomenda(chapeu , 3, 5, bicicleta, 12, rua(canas, adaufe), gustavo, tempo(2021,10,23,10), 2),
                        encomenda(gravata , 2, 3, bicicleta, 21, rua(maias, adaufe), gil, tempo(2021,11,30,1), 1)]).


%query4

estafeta(henrique, [encomenda(espada, 3, 10, bicicleta, 13, rua(gatao, espinho), heitor, tempo(2021,10,3,13), 4),
                     encomenda(lanca, 13, 40, mota, 16, rua(maias, adaufe), hugo, tempo(2021,11,6,9), 3),
                    encomenda(machado, 15, 25, carro, 19, rua(lameiros, espinho), hélio, tempo(2021,9,12,24), 5)]).


%query5

estafeta(ines, [encomenda(bola, 2, 1, bicicleta, 6, rua(gatao, espinho), igor, tempo(2021,11,10,21), 5),
              encomenda(rede, 5, 10, mota, 3, rua(canas, adaufe), dolores, tempo(2021,9,31,12), 2),
              encomenda(baliza, 25, 20, carro, 9, rua(maias, adaufe), marta, tempo(2021,10,23,1), 4),
              encomenda(chuteiras, 3, 15, mota, 7, rua(presa, arcozelo), ricardo, tempo(2021,11,16,7), 3),
              encomenda(tinta, 1, 10, bicicleta, 1, rua(lameiros, espinho), marcelo, tempo(2021,10,5,12), 1)]).

estafeta(juliana, [encomenda(papel, 1, 10, bicicleta, 2, rua(lameiros, gualtar), joao, tempo(2021,9,17,15), -1)]).

%COMO TESTAR
%1 - Testar com os estafetas todos: tem de dar rua "capa" e freguesia "gualtar"
%2 - Testar só com os estafetas da query5: tem de dar rua "lameiros" e freguesia "espinho"

%--------------------------------------------------------------------------------------------------------------------------------%

%query6
%COMO TESTAR
%1 - Testar com o q1bic: tem de dar "1"
%2 - Testar com o q1mota: tem de dar "3.666(6)"
%3 - Testar com o q3NewClient: Tem de dar "5"
%4 - Testar com o q5InvalidLocation: Tem de dar "-1"
%5 - Testar com o q5Location: tem de dar "1.6"


%--------------------------------------------------------------------------------------------------------------------------------%

%query7

%1 - Dia 1 para 24 horas: 5 bicicletas, 1 mota, 2 carros
%2 - Dia 1 para as 2 primeiras horas: tem de dar o mesmo de cima
%3 - Dia 1 para a 1a hora: Ou dá o mesmo de cima ou não dá nada (depende da implementação)
%4 - Dia 8 para whatever hora: Tem de dar 0 a tudo
%5 - Dia 11 para as 1as 12 horas: Tem de dar 0 bicicletas, 1 mota, 0 carro
%6 - Dia 9 a dia 13 (não sei se é suposto implementar isso): 1 bicicleta, 1 mota, 1 carro


%--------------------------------------------------------------------------------------------------------------------------------%

%query8

%1 - Dia 1 para 24 horas: 8 entregas (Nota: há um total de 11 encomendas mas uma tem classificação de -1 logo não foi entregue)
%2 - Dia 2 para as primeiras 12 horas: 4 entregas
%3 - Dia 2 entre as 12h e 20h: 2 ou 4 (depende da implementação, se a última hora é inclusive ou não)
%4 - Dia 10 nas 1as 10 horas : 1 entrega
%5 - Dia 9 a dia 13: 3 entregas
%6 - Dia 30 todo: 0 entregas


%--------------------------------------------------------------------------------------------------------------------------------%

%query9

%1 - Dia 1 para whatever horas: 10 concluídas, 1 não concluída
%2 - Dia 12 para whatever horas: 1 concluídas, 0 não concluídas
%3 - Dia 1 a dia 30: 26 concluídos, 1 não concluídas


%----------------------------------------------QUERY1------------------------------------------------------------------------------%

%query10

%1 - Testar com q1bic dia 1: 1 encomenda
%2 - Testar com q1bic dia 5: 0 encomendas
