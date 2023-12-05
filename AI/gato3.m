%% Juego del Gato Version 3
play = 1;
while ( play == 1 )
    Gato = [0 0 0 0 0 0 0 0 0];
    VD = [100.08 100.04 100.07 100.03 100.09 100.02 100.06 100.01 100.05];
    Turno = input('TURNO: (0 reinicia) (1 Maquina) (2 Humano) ');
    if ( Turno == 0 )
        disp('No lo haré')
%         caso1 = Gato;
%         caso2 = Gato;
%         caso3 = Gato;
%         caso4 = Gato;
%         caso5 = Gato;
%         caso6 = Gato;
%         caso7 = Gato;
%         caso8 = Gato;
%         caso9 = Gato;
%         escoger1 = VD;
%         escoger2 = VD;
%         escoger3 = VD;
%         escoger4 = VD;
%         escoger5 = VD;
%         escoger6 = VD;
%         escoger7 = VD;
%         escoger8 = VD;
%         escoger9 = VD;
%         Empate = 0;
    else
        load caso1
        load escoger1
        
        load caso2
        load escoger2
        
        load caso3
        load escoger3
        
        load caso4
        load escoger4
        
        load caso5
        load escoger5
        
        load caso6
        load escoger6
        
        load caso7
        load escoger7
        
        load caso8
        load escoger8
        
        load caso9
        load escoger9
        
        load Empate
        %% Tiro 1
        tiro = 1;
        Val = ( Gato < 1 );
        L = size( caso1 );
        capa1 = 0;
        sh = 0;
        while ( sh == 0 )
            capa1 = capa1+1;
            if (capa1 <= L)
                cs = isequal( Gato, caso1(capa1,:) );
                if cs == 1
                    sh = 1;
                end
            else
                caso1 = [caso1;Gato];
                escoger1 = [escoger1;VD];
                sh = 1;
            end
        end

        if (Turno == 1)
            display('Tiro de la maquina');
            [num,pos1] = max(escoger1(capa1,:).*Val);
            Gato(pos1) = 1;
            Turno = 2;
        else
            tablero = [Gato(1:3);Gato(4:6);Gato(7:9)]
            pos1=input('ingresa una posicion (1-9) ');
            while Val(pos1)<=0
                pos1 = input('ingresa una posicion (1-9) ');
            end
            Gato(pos1) = 2;
            Turno = 1;
        end
        tablero = [Gato(1:3);Gato(4:6);Gato(7:9)]
        %% Tiro 2
        tiro = 2;
        Val = (Gato<1);
        L = size(caso2);
        capa2 = 0;
        sh = 0;
        while sh==0
            capa2 = capa2+1;
            if ( capa2 <= L)
                cs = isequal(Gato,caso2(capa2,:));
                if (cs == 1)
                    sh = 1;
                end
            else
                caso2=[caso2;Gato];
                escoger2=[escoger2;VD];
                sh=1;
            end
        end

        if (Turno == 1)
            display('Tiro de la maquina');
            [num,pos2]=max(escoger2(capa2,:).*Val);
            Gato(pos2)=1;
            Turno=2;
        else
            pos2=input('ingresa una posicion (1-9) ');
            while Val(pos2)<=0
                pos2=input('ingresa una posicion (1-9) ');
            end
            Gato(pos2)=2;
            Turno=1;
        end
        tablero=[Gato(1:3);Gato(4:6);Gato(7:9)]
        %% Tiro 3
        tiro = 3;
        Val = (Gato<1);
        L = size(caso3);
        capa3 = 0;
        sh = 0;
        while sh==0
            capa3=capa3+1;
            if capa3 <= L
                cs = isequal(Gato,caso3(capa3,:));
                if cs==1
                    sh = 1;
                end
            else
                caso3 = [caso3;Gato];
                escoger3 = [escoger3;VD];
                sh = 1;
            end
        end

        if ( Turno == 1 )
            display('Tiro de la maquina');
            [num,pos3] = max(escoger3(capa3,:).*Val);
            Gato(pos3) = 1;
            Turno = 2;
        else
            pos3=input('ingresa una posicion (1-9) ');
            while Val(pos3)<=0
                pos3=input('ingresa una posicion (1-9) ');
            end
            Gato(pos3)=2;
            Turno=1;
        end
        tablero=[Gato(1:3);Gato(4:6);Gato(7:9)]
        %% Tiro 4
        tiro = 4;
        Val = (Gato<1);
        L = size(caso4);
        capa4 = 0;
        sh = 0;
        while sh==0
            capa4=capa4+1;
            if capa4<=L
                cs=isequal(Gato,caso4(capa4,:));
                if cs==1
                    sh=1;
                end
            else
                caso4=[caso4;Gato];
                escoger4=[escoger4;VD];
                sh=1;
            end
        end
        if ( Turno == 1 )
            display('Tiro de la maquina');
            [num,pos4]=max(escoger4(capa4,:).*Val);
            Gato(pos4)=1;
            Turno=2;
        else
            pos4 = input('ingresa una posicion (1-9) ');
            while Val(pos4)<=0
                pos4 = input('ingresa una posicion (1-9) ');
            end
            Gato(pos4) = 2;
            Turno = 1;
        end
        tablero = [Gato(1:3);Gato(4:6);Gato(7:9)]

        %% Tiro 5
        tiro = 5;
        Val = (Gato<1);
        L = size(caso5);
        capa5 = 0;
        sh = 0;
        while sh == 0
            capa5=capa5+1;
            if capa5<=L
                cs=isequal(Gato,caso5(capa5,:));
                if cs==1
                    sh=1;
                end
            else
                caso5 = [caso5;Gato];
                escoger5 = [escoger5;VD];
                sh = 1;
            end
        end

        if ( Turno == 1 )
            display('Tiro de la maquina');
            [num,pos5]=max(escoger5(capa5,:).*Val);
            Gato(pos5)=1;
            Turno=2;
        else
            pos5=input('ingresa una posicion (1-9) ');
            while Val(pos5)<=0
                pos5=input('ingresa una posicion (1-9) ');
            end
            Gato(pos5) = 2;
            Turno = 1;
        end
        tablero = [Gato(1:3);Gato(4:6);Gato(7:9)]
        VWIN = WIN(Gato);

        if VWIN == 0
            %% Tiro 6
            tiro = 6;
            Val = (Gato<1);
            L = size(caso6);
            capa6 = 0;
            sh = 0;
            while sh==0
                capa6=capa6+1;
                if capa6<=L
                    cs = isequal(Gato,caso6(capa6,:));
                    if cs==1
                        sh = 1;
                    end
                else
                    caso6 = [caso6;Gato];
                    escoger6 = [escoger6;VD];
                    sh = 1;
                end
            end

            if (Turno == 1)
                display('Tiro de la maquina');
                [num,pos6]=max(escoger6(capa6,:).*Val);
                Gato(pos6)=1;
                Turno=2;
            else
                pos6=input('ingresa una posicion (1-9) ');
                while Val(pos6)<=0
                    pos6=input('ingresa una posicion (1-9) ');
                end
                Gato(pos6)=2;
                Turno=1;
            end
            tablero = [Gato(1:3);Gato(4:6);Gato(7:9)]
            VWIN = WIN(Gato);

            if ( VWIN == 0 )
                %% Tiro 7
                tiro = 7;
                Val = (Gato<1);
                L = size(caso7);
                capa7 = 0;
                sh = 0;
                while sh==0
                    capa7=capa7+1;
                    if capa7<=L
                        cs=isequal(Gato,caso7(capa7,:));
                        if cs==1
                            sh=1;
                        end
                    else
                        caso7 = [caso7;Gato];
                        escoger7 = [escoger7;VD];
                        sh = 1;
                    end
                end

                if ( Turno == 1 )
                    display('Tiro de la maquina');
                    [num,pos7]=max(escoger7(capa7,:).*Val);
                    Gato(pos7)=1;
                    Turno=2;
                else
                    pos7=input('ingresa una posicion (1-9) ');
                    while Val(pos7)<=0
                        pos7=input('ingresa una posicion (1-9) ');
                    end
                    Gato(pos7) = 2;
                    Turno = 1;
                end
                tablero=[Gato(1:3);Gato(4:6);Gato(7:9)]
                VWIN=WIN(Gato);

            if VWIN==0
                %% Tiro 8
                tiro=8;
                Val=(Gato<1);
                L=size(caso8);
                capa8=0;sh=0;
                while sh==0
                    capa8=capa8+1;
                    if capa8<=L
                        cs=isequal(Gato,caso8(capa8,:));
                        if cs==1
                            sh=1;
                        end
                    else
                        caso8=[caso8;Gato];
                        escoger8=[escoger8;VD];
                        sh=1;
                    end
                end
    
                if ( Turno == 1 )
                    display('Tiro de la maquina');
                    [num,pos8]=max(escoger8(capa8,:).*Val);
                    Gato(pos8)=1;
                    Turno=2;
                else
                    pos8=input('ingresa una posicion (1-9) ');
                    while Val(pos8)<=0
                        pos8=input('ingresa una posicion (1-9) ');
                    end
                    Gato(pos8)=2;
                    Turno=1;
                end
                tablero=[Gato(1:3);Gato(4:6);Gato(7:9)]
                VWIN=WIN(Gato);
    
                if VWIN==0
                    %% Tiro 9
                    tiro = 9;
                    Val = (Gato<1);
                    L = size(caso9);
                    capa9 = 0;
                    sh = 0;
                    while sh==0
                        capa9=capa9+1;
                        if capa9<=L
                            cs=isequal(Gato,caso9(capa9,:));
                            if cs==1
                                sh=1;
                            end
                        else
                            caso9=[caso9;Gato];
                            escoger9=[escoger9;VD];
                            Empate(capa9)=0;
                            sh=1;
                        end
                    end
    
                    if ( Turno == 1 )
                        display('Tiro de la maquina');
                        [num,pos9]=max(escoger9(capa9,:).*Val);
                        Gato(pos9)=1;
                        Turno=2;
                    else
                        pos9=input('ingresa una posicion (1-9) ');
                        while Val(pos9)<=0
                            pos9=input('ingresa una posicion (1-9) ');
                        end
                        Gato(pos9) = 2;
                        Turno = 1;
                    end
                    tablero = [Gato(1:3);Gato(4:6);Gato(7:9)]
                    VWIN = WIN(Gato);
                end
            end
        end
    end
        if (VWIN == 1)
            display('Gana Maquina');
        elseif (VWIN == 2)
            display('Gana Humano');
        else
            display('Empate');
            Empate(capa9) = Empate(capa9) + 1;
        end
    
        %% Aprendizaje
        if VWIN == 0 && Empate(capa9) <= 5 %por la clase +0.15
            escoger1(capa1,pos1) = escoger1(capa1,pos1) + .0025; %+~ aprendizaje en cada empate
            escoger2(capa2,pos2) = escoger2(capa2,pos2) + .0025;
            escoger3(capa3,pos3) = escoger3(capa3,pos3) + .0025;
            escoger4(capa4,pos4) = escoger4(capa4,pos4) + .0025;
            escoger5(capa5,pos5) = escoger5(capa5,pos5) + .0025;
            if tiro>=6
                escoger6(capa6,pos6)=escoger6(capa6,pos6)+.0025;
                if tiro>=7
                    escoger7(capa7,pos7)=escoger7(capa7,pos7)+.0025;
                    if tiro>=8
                        escoger8(capa8,pos8)=escoger8(capa8,pos8)+.0025;
                        if tiro>=9
                            escoger9(capa9,pos9)=escoger9(capa9,pos9)+.0025;
                        end
                    end
                end
            end
        elseif VWIN == 0 && Empate(capa9) > 5
            escoger1(capa1,pos1) = escoger1(capa1,pos1) - .01/Empate(capa9);
            escoger2(capa2,pos2) = escoger2(capa2,pos2) - .01/Empate(capa9);
            escoger3(capa3,pos3) = escoger3(capa3,pos3) - .04/Empate(capa9);
            escoger4(capa4,pos4) = escoger4(capa4,pos4) - .05/Empate(capa9);
            escoger5(capa5,pos5) = escoger5(capa5,pos5) - .06/Empate(capa9);
            if tiro>=6
                escoger6(capa6,pos6)=escoger6(capa6,pos6)-.06/Empate(capa9);
                if tiro>=7
                    escoger7(capa7,pos7)=escoger7(capa7,pos7)-.05/Empate(capa9);
                    if tiro>=8
                        escoger8(capa8,pos8)=escoger8(capa8,pos8)-.04/Empate(capa9);
                        if tiro>=9
                            escoger9(capa9,pos9)=escoger9(capa9,pos9)-.0025/Empate(capa9);
                        end
                    end
                end
            end
        elseif mod(tiro,2)==1 %impar
            escoger1(capa1,pos1)=escoger1(capa1,pos1)+.01;
            escoger2(capa2,pos2)=escoger2(capa2,pos2)-.01;
            escoger3(capa3,pos3)=escoger3(capa3,pos3)+.04;
            escoger4(capa4,pos4)=escoger4(capa4,pos4)-.05;
            escoger5(capa5,pos5)=escoger5(capa5,pos5)+.06;
            if tiro>=6
                escoger6(capa6,pos6)=escoger6(capa6,pos6)-.06;
                if tiro>=7
                    escoger7(capa7,pos7)=escoger7(capa7,pos7)+.05;
                    if tiro>=8
                        escoger8(capa8,pos8)=escoger8(capa8,pos8)-.04;
                        if tiro>=9
                            escoger9(capa9,pos9)=escoger9(capa9,pos9)+.0025;
                        end
                    end
                end
            end
        elseif mod(tiro,2)==0 %par
            escoger1(capa1,pos1)=escoger1(capa1,pos1)-.01;
            escoger2(capa2,pos2)=escoger2(capa2,pos2)+.01;
            escoger3(capa3,pos3)=escoger3(capa3,pos3)-.04;
            escoger4(capa4,pos4)=escoger4(capa4,pos4)+.05;
            escoger5(capa5,pos5)=escoger5(capa5,pos5)-.06;
            if tiro>=6
                escoger6(capa6,pos6)=escoger6(capa6,pos6)+.06;
                if tiro>=7
                    escoger7(capa7,pos7)=escoger7(capa7,pos7)-.05;
                    if tiro>=8
                        escoger8(capa8,pos8) = escoger8(capa8,pos8) + .04;
                        if tiro>=9
                            escoger9(capa9,pos9) = escoger9(capa9,pos9) - .0025;
                        end
                    end
                end
            end
        end
    end

    save('caso1', 'caso1');
    save('escoger1', 'escoger1');

    save('caso2', 'caso2');
    save('escoger2', 'escoger2');

    save('caso3', 'caso3');
    save('escoger3', 'escoger3');

    save('caso4', 'caso4');
    save('escoger4', 'escoger4');

    save('caso5', 'caso5');
    save('escoger5', 'escoger5');

    save('caso6', 'caso6');
    save('escoger6', 'escoger6');

    save('caso7', 'caso7');
    save('escoger7', 'escoger7');

    save('caso8', 'caso8');
    save('escoger8', 'escoger8');

    save('caso9', 'caso9');
    save('escoger9', 'escoger9');

    save('Empate', 'Empate');
    play = input('¿quieres jugar de nuevo? (si = 1) ');
end