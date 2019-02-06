
#include <stdbool.h>

// Represents number of children for each node in a trie
#define N 27
// Represents a node in a trie
typedef struct node
{
    bool is_word;
    struct node *children[N];
}
node;

// Trie Prototypes
node* insert (node* _root, const char* word);
int search (node* _root, const char* word);
bool destroy (node* *current_node);