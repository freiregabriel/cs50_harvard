#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "trie.h"


int main(void) {
    node* root = malloc(sizeof(node));
    root->is_word = 0;
    for (int i = 0; i < N; i++) {
        root->children[i] = NULL;
    }
    printf("will insert");
    root = insert(root, "dog");
    root = insert(root, "do");
    root = insert(root, "dont");
    printf("Contains do ? %i\n", search(root, "do"));
    printf("Contains dog ? %i\n", search(root, "dog"));
    printf("Contains dont ? %i\n", search(root, "dont"));
    printf("freeing...\n");
    destroy(&root);
    printf("freed....\n");
    // free(root);
}

node* _make_node () {
    node* new_letter = malloc(sizeof(node));
    if (new_letter == NULL ) {
        return NULL;
    }
    new_letter->is_word = 0;
    for (int i = 0; i < N; i++) {
        new_letter->children[i] = NULL;
    }
    return new_letter;
}
node* insert (node* root, const char* word) {
    node* tmp = root;
    while (*word) {
        int letter_idx = isupper(*word) ? *word - 'A' : *word - 'a';
        if (tmp->children[letter_idx] == NULL) {
            node* new_letter = _make_node();
            if (new_letter == NULL) {
                printf("out of memory");
                break;
            }
            tmp->children[letter_idx] = new_letter;
            tmp = new_letter;
        } else {
            tmp = tmp->children[letter_idx];
        }
        word++;
    }
    tmp->is_word = 1;
    return root;
}

int search (node* root, const char* word) {
    if (root == NULL) {
        return 0;
    }
    node* tmp = root;
    while (*word) {
        int letter_index = isupper(*word) ? *word - 'A' : *word - 'a';
        tmp = tmp->children[letter_index];
        if(tmp == NULL) {
            return 0;
        }
        word++;
    }
    return tmp->is_word; // found, check if its a word
}

bool destroy (node* *current_node) {
    if (current_node == NULL || *current_node == NULL) {
        return false;
    }
    for (int i = 0; i < N; i++) {
        // printf("%i\n", i);
        destroy(&((*current_node)->children[i]));
    }
    free(*current_node);
    return true;

}