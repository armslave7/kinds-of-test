DIR_SRC = ./
DIR_OBJ = ./obj
DIR_BIN = ./

SRC = $(wildcard ${DIR_SRC}*.f90)  
OBJ = $(patsubst %.f90,${DIR_OBJ}/%.o,$(notdir ${SRC}))

TARGET = main

BIN_TARGET = ${DIR_BIN}${TARGET}

CC = gfortran

CFLAGS = -Wall -O2

${BIN_TARGET}: ${OBJ}
	$(CC) $(OBJ)  -o $@

${DIR_OBJ}/%.o:${DIR_SRC}%.f90
	$(CC) $(CFLAGS) -c  $< -o $@

.PHONY:clean

clean:
	rm $(DIR_OBJ)/*.o