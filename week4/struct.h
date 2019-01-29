typedef struct {
    char* name;
    char* dorm;
}
student;


typedef struct node {
    int n;
    struct node* next;
}node;

typedef struct {
    struct node* nodes;
    int head;
    int tail;
}LinkedList;