#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "trie.h"

t_node* insert (t_node* root, char* word);
int search (t_node* root, char* word);
void destroy (t_node* *current_node);

int main(void) {
    t_node* root = malloc(sizeof(t_node));
    root->is_word = 0;
    root = insert(root, "dog");
    root = insert(root, "do");
    root = insert(root, "dont");
    printf("Contains do ? %i\n", search(root, "do"));
    printf("Contains dog ? %i\n", search(root, "dog"));
    printf("Contains dont ? %i\n", search(root, "dont"));
    printf("freeing...");
    destroy(&root);
    printf("freed....");
    // free(root);
}
t_node* insert (t_node* root, char* word) {
    int n = strlen(word);
    t_node* tmp = root;
    while (*word) {
        int letter_idx = isupper(*word) ? *word - 'A' : *word - 'a';
        if (tmp->children[letter_idx] != NULL) {
            tmp = tmp->children[letter_idx];
        } else {
            t_node* new_letter = malloc(sizeof(t_node));
            if (new_letter == NULL ) {
                printf("out of memory");
                break;
            }
            new_letter->is_word = 0;
            for (int i = 0; i < 27; i++) {
                new_letter->children[i] = NULL;
            }
            tmp->children[letter_idx] = new_letter;
            tmp = new_letter;
        }
        word++;
    }
    tmp->is_word = 1;
    return root;
}

int search (t_node* root, char* word) {
    if (root == NULL) {
        return 0;
    }
    t_node* tmp = root;
    while (*word) {
        tmp = tmp->children[*word - 'a'];
        if(tmp == NULL) {
            return 0;
        }
        word++;
    }
    return tmp->is_word; // found, check if its a word
}

int hasChildren (t_node* node) {
    for (int i = 0; i < 27; i++) {
        if (node->children[i]) {
            return 1;
        }
    }
    return 0;
}

void destroy (t_node* *current_node) {
    int i;
    if (current_node == NULL || *current_node == NULL) {
        return;
    }
    for (i = 0; i < 27; i++) {
        printf("%i\n", i);
        destroy(&((*current_node)->children[i]));
    }
    free(*current_node);
    
}