#include <pthread.h>
#include <stdio.h>


void* app(void*){
    system("python3 app.py 6100");
}

void* gui(void*){
    system("python3 gui/gui.py localhost:6101 http://localhost:6100");
}

void* trainer(void*){
    system("python3 trainer/trainer.py localhost:6102 http://localhost:6100");
}

void* assembler(void*){
    system("python3 assembler/assembler.py localhost:6103 http://localhost:6100");
}

int main() {
    pthread_t tid;
    pthread_create(&tid, NULL, &app, NULL);
    pthread_create(&tid, NULL, &gui, NULL);
    pthread_create(&tid, NULL, &trainer, NULL);
    pthread_create(&tid, NULL, &assembler, NULL);

    pthread_join(tid, NULL);
}
