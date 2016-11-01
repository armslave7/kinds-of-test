objs = fun.o hello.o

dir_obj = ./obj/

obj = $(addprefix $(dir_obj),$(objs))

CC = gfortran

cflags = -Wall -O2

hello.exe: $(obj)
	gfortran $(obj) -o dc3d.exe

$(dir_obj)%.o: %.f90
	$(CC) -c $(cflags) $< -o $@
