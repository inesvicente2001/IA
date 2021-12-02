:- include('BaseConhecimento.pl').


:- dynamic cliente/2.
:- dynamic rua/2.
:- dynamic tempo/4.
:- dynamic encomenda/8.
:- dynamic estafeta/2.


ecologicidade(bicicleta, 2).
ecologicidade(mota, 1).
ecologicidade(carro, 0).

%----------------------------------------------QUERY1------------------------------------------------------------------------------%

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

query4(ValorFinal,Ano,Mes,Dia) :-
    findall(
        Valor,
        (
            estafeta(_,Encomendas),
            member(encomenda(_,Peso,Volume,Transporte,Prazo,_,_,tempo(Ano,Mes,Dia,_),Classificacao), Encomendas),
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
    
%----------------------------------------------QUERY6------------------------------------------------------------------------------%

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

pertence_tempo(tempo(AnoI,_,_,_),tempo(AnoF,_,_,_),tempo(Ano,_,_,_)) :-
    Ano > AnoI,
    Ano < AnoF.
pertence_tempo(tempo(AnoI,MesI,_,_),tempo(AnoF,_,_,_),tempo(AnoI,Mes,_,_)) :-
    AnoF > AnoI,
    Mes > MesI.
pertence_tempo(tempo(AnoI,Mes,DiaI,_),tempo(AnoF,_,_,_),tempo(AnoI,Mes,Dia,_)) :-
    AnoF > AnoI,
    Dia > DiaI.
pertence_tempo(tempo(AnoI,Mes,Dia,HoraI),tempo(AnoF,_,_,_),tempo(AnoI,Mes,Dia,Hora)) :-
    AnoF > AnoI,
    Hora >= HoraI.
pertence_tempo(tempo(AnoI,_,_,_),tempo(AnoF,MesF,_,_),tempo(AnoF,Mes,_,_)) :-
    AnoF > AnoI,
    Mes < MesF.
pertence_tempo(tempo(AnoI,_,_,_),tempo(AnoF,Mes,DiaF,_),tempo(AnoF,Mes,Dia,_)) :-
    AnoF > AnoI,
    Dia < DiaF.
pertence_tempo(tempo(AnoI,_,_,_),tempo(AnoF,Mes,Dia,HoraF),tempo(AnoF,Mes,Dia,Hora)) :-
    AnoF > AnoI,
    Hora =< HoraF.
pertence_tempo(tempo(Ano,MesI,_,_),tempo(Ano,MesF,_,_),tempo(Ano,Mes,_,_)) :-
    Mes > MesI,
    Mes < MesF.
pertence_tempo(tempo(Ano,MesI,DiaI,_),tempo(Ano,MesF,_,_),tempo(Ano,MesI,Dia,_)) :-
    MesF > MesI,
    Dia > DiaI.
pertence_tempo(tempo(Ano,MesI,Dia,HoraI),tempo(Ano,MesF,_,_),tempo(Ano,MesI,Dia,Hora)) :-
    MesF > MesI,
    Hora >= HoraI.
pertence_tempo(tempo(Ano,MesI,_,_),tempo(Ano,MesF,DiaF,_),tempo(Ano,MesF,Dia,_)) :-
    MesF > MesI,
    Dia < DiaF.
pertence_tempo(tempo(Ano,MesI,_,_),tempo(Ano,MesF,Dia,HoraF),tempo(Ano,MesF,Dia,Hora)) :-
    MesF > MesI,
    Hora =< HoraF.
pertence_tempo(tempo(Ano,Mes,DiaI,_),tempo(Ano,Mes,DiaF,_),tempo(Ano,Mes,Dia,_)) :-
    Dia > DiaI,
    Dia < DiaF.
pertence_tempo(tempo(Ano,Mes,Dia,HoraI),tempo(Ano,Mes,Dia,HoraF),tempo(Ano,Mes,Dia,Hora)) :-
    Hora >= HoraI,
    Hora =< HoraF.
pertence_tempo(tempo(Ano,Mes,DiaI,HoraI),tempo(Ano,Mes,DiaF,_),tempo(Ano,Mes,DiaI,Hora)) :-
    DiaI < DiaF,
    Hora >= HoraI.
pertence_tempo(tempo(Ano,Mes,DiaI,_),tempo(Ano,Mes,DiaF,HoraF),tempo(Ano,Mes,DiaF,Hora)) :-
    DiaI < DiaF,
    Hora =< HoraF.
pertence_tempo(tempo(Ano,Mes,Dia,Hora),tempo(Ano,Mes,Dia,Hora),tempo(Ano,Mes,Dia,Hora)).

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
    
%----------------------------------------------QUERY10-----------------------------------------------------------------------------%

query10(Pesos,Ano,Mes,Dia) :-
    findall(
        Nome/Peso,
        (
            estafeta(Nome,Encomendas),
            findall(
                P,
                (
                    member(encomenda(_,P,_,_,_,_,_,tempo(Ano,Mes,Dia,_),_),Encomendas)
                ),
                LP
            ),
            sum_list(LP, Peso)
        ),
        Pesos
    ).

%----------------------------------------------QUERY11-----------------------------------------------------------------------------%

%Ver qual o cliente que pediu mais encomendas num certo período de tempo

query11(ClienteMax,Inicio,Fim) :-
    findall(
        Cliente,
        (
            estafeta(_, Encomendas),
            member(encomenda(_,_,_,_,_,_,Cliente,Tempo,_), Encomendas),
            pertence_tempo(Inicio,Fim,Tempo)
        ),
        LEncomendas
    ),
    flatten(LEncomendas, Flatten),
    aggregate(max(C,E),aggregate(count,member(E,Flatten),C),max(_, ClienteMax)).



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