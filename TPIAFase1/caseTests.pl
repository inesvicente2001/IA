
:- dynamic cliente/2.
:- dynamic rua/2.
:- dynamic tempo/2.
:- dynamic encomenda/8.
:- dynamic estafeta/2.

%rua(capa, gualtar).
%rua(vicente, gualtar).
%rua(bouca, gualtar).
%rua(sol, gualtar).
%rua(fonte, gualtar).
%rua(presa, adaufe).
%rua(quintao, adaufe).
%rua(maias, adaufe).
%rua(canas, adaufe).
%rua(rochas, adaufe).
%rua(gatao, espinho).
%rua(paco, espinho).
%rua(clamor, espinho).
%rua(lameiros, espinho).
%rua(regadas, espinho).
%rua(costa, arcozelo).
%rua(aflitos, arcozelo).
%rua(presa, arcozelo).
%rua(jaca, arcozelo).
%rua(granja, arcozelo).
%rua(rio, burgaes).
%rua(alegria, burgaes).
%rua(bela, burgaes).
%rua(colonias, burgaes).
%rua(padassas, burgaes).
velocidade(bicicleta, 10).
velocidade(mota, 35).
velocidade(carro, 25).

capacidade(bicicleta, 5).
capacidade(mota, 20).
capacidade(carro, 100).


%query 1
estafeta(q1bic, [encomenda(camisola, 1, 1, bicicleta, 1, rua(capa, gualtar), passas, tempo(1,1), 1), 
                 encomenda(piano, 1, 1, bicicleta, 1, rua(capa, gualtar), esperanca, tempo(3,1), 1), 
                 encomenda(camisola, 1, 1, bicicleta, 1, rua(capa, gualtar), passas, tempo(2,1), 1)]).


estafeta(q1mota, [encomenda(camisola, 1, 1, mota, 1, rua(capa, gualtar), esperanca, tempo(1,1), 3),
                  encomenda(camisola, 1, 1, mota, 1, rua(capa, gualtar), esperanca, tempo(2,3), 5),
                  encomenda(camisola, 1, 1, mota, 1, rua(capa, gualtar), esperanca, tempo(2,6), 3)]).


estafeta(q1carro, [encomenda(camisa, 1, 1, carro, 1, rua(capa, gualtar), passas, tempo(1,1), 3),
                   encomenda(camisa, 1, 1, carro, 1, rua(capa, gualtar), passas, tempo(3,1), 3),
                   encomenda(meias, 1, 1, carro, 1, rua(capa, gualtar), passas, tempo(2,10), 3)]).

estafeta(q1mixed, [encomenda(camisola, 1, 1, bicicleta, 1, rua(capa, gualtar), passas, tempo(2,14), 3),
                   encomenda(camisola, 1, 1, mota, 1, rua(capa, gualtar), esperanca, tempo(2,15), 3),
                   encomenda(camisola, 1, 1, carro, 1, rua(capa, gualtar), esperanca, tempo(1,1), 3)]).

estafeta(q1OneBic, [encomenda(saco,1, 1, bicicleta, 1, rua(capa, gualtar), passas, tempo(3,1), 3)]).

%query3

estafeta(q3NewClient, [encomenda(camisola, 1, 1, bicicleta, 1, rua(capa, gualtar), novais, tempo(2,18), 5)]).

estafeta(q3AllClients, [encomenda(camisola, 1, 1, bicicleta, 1, rua(capa, gualtar), passas, tempo(1,1), 3),
                        encomenda(camisola, 1, 1, bicicleta, 1, rua(capa, gualtar), esperanca, tempo(2,20), 3),
                        encomenda(camisola, 1, 1, bicicleta, 1, rua(capa, gualtar), novais, tempo(3,1), 3),
                        encomenda(camisola, 1, 1, bicicleta, 1, rua(capa, gualtar), ines, tempo(3,1), 3)]).


%query4

estafeta(q4OneDate, [encomenda(camisola, 1, 1, bicicleta, 1, rua(capa, gualtar), passas, tempo(10,1), 3),
                     encomenda(camisola, 1, 1, mota, 1, rua(capa, gualtar), passas, tempo(11,1), 3),
                    encomenda(camisola, 1, 1, carro, 1, rua(capa, gualtar), passas, tempo(12,1), 3)]).


%query5

estafeta(q5Location, [encomenda(camisola, 1, 1, bicicleta, 1, rua(gatao, espinho), passas, tempo(1,1), -1),
              encomenda(camisola, 1, 1, bicicleta, 1, rua(gatao, espinho), passas, tempo(1,1), 2),
              encomenda(camisola, 1, 1, bicicleta, 1, rua(lameiros, espinho), passas, tempo(1,1), -1),
              encomenda(camisola, 1, 1, bicicleta, 1, rua(lameiros, espinho), passas, tempo(1,1), 5),
              encomenda(camisola, 1, 1, bicicleta, 1, rua(lameiros, espinho), passas, tempo(1,1), 3)]).

estafeta(q5InvalidLocation, [encomenda(camisola, 1, 1, bicicleta, 1, rua(lameiros, gualtar), passas, tempo(1,1), -1)]).

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

ecologicidade(bicicleta, 2).
ecologicidade(mota, 1).
ecologicidade(carro, 0).

maximo(X1/Y1, _/Y2, X1/Y1) :- Y1 >= Y2, !.
maximo(_/Y1, X2/Y2, X2/Y2) :- Y2 > Y1, !.


query1(Estafeta) :-
    findall(
        Nome/ValorFinal,
        (
            estafeta(Nome, Encomendas),
            findall(
                Valor,
                (
                    member(encomenda(_,_,_,T,_,_,_,_,_), Encomendas),
                    ecologicidade(T, Valor)
                ),
                Valores
            ),
            sum_list(Valores, ValorFinal)
        ),
        [H|T]
    ),
    foldl(maximo, T, H, Estafeta/N).

%----------------------------------------------QUERY2------------------------------------------------------------------------------%



query2(LNomeEstafeta,LNomeEncomenda,Cliente) :-
    findall(
        Nome,
        (
            estafeta(Nome,Encomendas),
            %estafetas_entregaram(estafeta(Nome,Encomendas),LNomeEncomenda,Cliente)
            findall(
                Estafeta,
                (
                    member(encomenda(NomeEncomenda,_,_,_,_,_,Cliente,_,_),Encomendas),
                    member(NomeEncomenda,LNomeEncomenda)
                ),
                LEstafeta
            ),
            member(estafeta(Nome,Encomendas),LEstafeta)
        ),
        LNomeEstafetaAux
    ),
    sort(LNomeEstafetaAux, LNomeEstafeta).

%----------------------------------------------QUERY3------------------------------------------------------------------------------%

query3(Clientes, Nome) :-
    findall(
        Cliente,
        (
            estafeta(Nome, Encomendas),
            member(encomenda(_,_,_,_,_,_,Cliente,_,_), Encomendas)
        ), 
        ClientesAux
    ),
    sort(ClientesAux, Clientes).
    


%----------------------------------------------QUERY4------------------------------------------------------------------------------%

query4(ValorFinal,Dia) :-
    findall(
        Valor,
        (
            estafeta(_,Encomendas),
            member(encomenda(_,Peso,Volume,Transporte,Prazo,_,_,tempo(Dia,_),Classificacao), Encomendas),
            Classificacao > -1,
            preco_encomenda(Valor,Peso,Volume,Transporte,Prazo)
        ),
        Valores
    ),
    sum_list(Valores, ValorFinal).

preco_encomenda(Valor,Peso, Volume, carro, Prazo) :-
    Valor = (20 * Peso * Volume) / Prazo.
preco_encomenda(Valor,Peso, Volume, mota, Prazo) :-
    Valor = (15 * Peso * Volume) / Prazo.
preco_encomenda(Valor, Peso, Volume, bicicleta, Prazo) :-
    Valor = (10 * Peso * Volume) / Prazo.
%----------------------------------------------QUERY5------------------------------------------------------------------------------%

query5(ZonaMax,freguesia) :-
    findall(
        Freguesia,
        (
            estafeta(_, Encomendas),
            member(encomenda(_,_,_,_,_,rua(_,Freguesia),_,_,_), Encomendas)
        ),
        LEncomendas
    ),
    flatten(LEncomendas, Flatten),
    aggregate(max(C,E),aggregate(count,member(E,Flatten),C),max(_, ZonaMax)).


query5(ZonaMax,rua) :-
    findall(
        Rua,
        (
            estafeta(_, Encomendas),
            member(encomenda(_,_,_,_,_,rua(Rua,_),_,_,_), Encomendas)
        ),
        LEncomendas
    ),
    flatten(LEncomendas, Flatten),
    aggregate(max(C,E),aggregate(count,member(E,Flatten),C),max(_, ZonaMax)).
%query5(ZonaMax,freguesia) :-
%    findall(
%        Freguesia/ValorZona,
%        (
%            findall(
%                Nome,
%                (
%                    findall(
%                        Encomendas,
%                        (
%                            estafeta(_, Encomendas)
%                        ),
%                        LEncomendas
%                    ),
%                    flatten(LEncomendas, LEncomenda),
%                    member(encomenda(Nome,_,_,_,_,rua(_,Freguesia),_,_,Class), LEncomenda),
%                    Class \= (-1)
%                ),
%                Valores
%            ),
%            length(Valores, ValorZona)
%        ),
%        [H|T]
%    ),
%    foldl(maximo, T, H, ZonaMax).

query6(Media, Nome) :-
    findall(
        Nota,
        (
            estafeta(Nome, Encomendas),
            member(encomenda(_,_,_,_,_,_,_,_,Nota), Encomendas)
        ),
        Classificacoes
    ),
    sum_list(Classificacoes, Sum),
    length(Classificacoes, Length),
    Length > 0,
    Media is Sum/Length.



    %fazer média da lista

%----------------------------------------------QUERY7------------------------------------------------------------------------------%
query7(NCarro,NMota,NBicicleta,Inicio,Fim) :-
    findall(
        Nome,
        (
            estafeta(_, Encomendas),
            member(encomenda(Nome,_,_,carro,_,_,_,Tempo,Class),Encomendas),
            Class \= (-1),
            pertence_tempo(Inicio,Fim,Tempo)
        ),
        LEntregasCarro
    ),
    findall(
        Nome,
        (
            estafeta(_, Encomendas),
            member(encomenda(Nome,_,_,mota,_,_,_,Tempo,Class),Encomendas),
            Class \= (-1),
            pertence_tempo(Inicio,Fim,Tempo)
        ),
        LEntregasMota
    ),
    findall(
        Nome,
        (
            estafeta(_, Encomendas),
            member(encomenda(Nome,_,_,bicicleta,_,_,_,Tempo,Class),Encomendas),
            Class \= (-1),
            pertence_tempo(Inicio,Fim,Tempo)
        ),
        LEntregasBicicleta
    ),
    length(LEntregasCarro,NCarro),
    length(LEntregasMota,NMota),
    length(LEntregasBicicleta,NBicicleta).

%----------------------------------------------QUERY8------------------------------------------------------------------------------%
pertence_tempo(tempo(DiaI,_),tempo(DiaF,_),tempo(Dia,_)) :-
    Dia > DiaI,
    Dia < DiaF.
pertence_tempo(tempo(DiaI,HoraI),tempo(DiaI,HoraF),tempo(DiaI,Hora)) :-
    Hora >= HoraI,
    Hora =< HoraF.
pertence_tempo(tempo(DiaI,HoraI),tempo(DiaF,_),tempo(DiaI,Hora)) :-
    Hora >= HoraI.
pertence_tempo(tempo(DiaI,_),tempo(DiaF,HoraF),tempo(DiaF,Hora)) :-
    Hora =< HoraF.

query8(NEntregas, Inicio, Fim):-
    findall(
        Classificacao,
        (
            estafeta(_, Encomendas),
            member(encomenda(_,_,_,_,_,_,_,Tempo,Classificacao), Encomendas),
            Classificacao > -1,
            pertence_tempo(Inicio, Fim, Tempo)
        ),
        Classificacoes
    ),
    length(Classificacoes, NEntregas).

%----------------------------------------------QUERY9------------------------------------------------------------------------------%
query9(NEntregasValida, NEntregasInvalidas, Inicio, Fim):-
    findall(
        Classificacao,
        (
            estafeta(_, Encomendas),
            member(encomenda(_,_,_,_,_,_,_,Tempo,Classificacao), Encomendas),
            Classificacao > -1,
            pertence_tempo(Inicio, Fim, Tempo)
        ),
        Classificacoes
    ),
    findall(
        Classificacao2,
        (
            estafeta(_, Encomendas2),
            member(encomenda(_,_,_,_,_,_,_,Tempo2,Classificacao2), Encomendas2),
            Classificacao2 = -1,
            pertence_tempo(Inicio, Fim, Tempo2)
        ),
        Classificacoes2
    ),
    length(Classificacoes, NEntregasValida),
    length(Classificacoes2, NEntregasInvalidas).
    
%query10

%----------------------------------------------QUERY10-----------------------------------------------------------------------------%

query10(Pesos,Dia) :-
    findall(
        Nome/Peso,
        (
            estafeta(Nome,Encomendas),
            findall(
                P,
                (
                    member(encomenda(_,P,_,_,_,_,_,tempo(Dia,_),_),Encomendas)
                ),
                LP
            ),
            sum_list(LP, Peso)
        ),
        Pesos
    ).

add_estafeta(L,Nome,Encomenda) :-
    findall(
        Name,
        estafeta(Nome,_),
        LNome
    ),
    member(Nome, LNome),
    estafeta(Nome, Package),
    append(Package, [Encomenda], NewList),
    retract(estafeta(Nome, Package)),
    assertz(estafeta(Nome, NewList)).


add_estafeta(L,Nome,Encomenda) :-
    findall(
        Name,
        estafeta(Nome,_),
        LNome
    ),
    not(member(Nome, LNome)),
    assertz(estafeta(Nome,[Encomenda])).

%retract



