# nandgame_script
This script produces assembly language code to draw picture for nandgame.com.
You should specify name of file with image description where "*" means colored pixel and "-" - the transparent one.

Script run example:
>python3 img2asm.py house.txt

File example (you don't need line numbers):
>        --------------------------------------------   0
>        ----------------*---------------------------   1
>        --------------------------------------------   2
>        ----*----------------*----------------*-----   3
>        ---------------------*----------------------   4
>        --------------------*-----------------------   5
>        ----------*--------**-----------------------   6
>        -*----------------***-----------------------   7
>        ------------------****-------*--------------   8
>        ------------------*****----------**---------   9
>        -----------*-------*****--------****--------   10
>        -----------*---------***--------****--------   11
>        -----------*----------**---------**------*--   12
>        -----*----***---------*-----*---------------   13
>        -----------*--------------------------------   14
>        ----------*--*-------***--------------------   15
>        ---------****-*---***-**********------------   16
>        ---------*****---****---*********-----------   17
>        -------******-*-******************----------   18
>        ---------**--***-*************--***--*------   19
>        -*------*---****-***********------**--------   20
>        ------*********---*********--------*--------   21
>        --------*****---*--********---**---**-------   22
>        -----**---*--*****---*****----**----*------*   23
>        ----****---*********--***---------*---*-----   24
>        ---------**--******----*----------*---*-----   25
>        ------*******---------------*-----*****-----   26
>        ----*--*******---***--------*******---*-----   27
>        *-****---**----******-*******-----*---------   28
>        ---*****----*******---------******----------   29
>        ----*******--***----**--*****---------------   30
>        -----------**------*****----*---------------   31
>        ---***---**--**********------*--------------   32
>        ********--************----***--*------------   33
>        -*********--***---***---***----*------------   34
>        ---********----***----**-*---**-**----------   35
>        ------*********-----***-*-----***-----------   36
>        ------------------**---*----**---**---------   37
>        --------------****---**------*****----------   38
>        ------------**----***-------*--*--*---------   39
>        ---------***-----**-------*****-*****-------   40
>        -------**-------*----------*********--------   41
>        *******-------****-----------*****----------   42
>        ------------****----------------------------   43
