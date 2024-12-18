#include <unistd.h>
#include <fcntl.h>

int main() {
    int fd[10];
    for (int i = 0; i < 10; i++) {
        fd[i] = open("flag.txt", O_RDONLY);
        printf("fd[%d] = %d\n", i, fd[i]);
    }
}