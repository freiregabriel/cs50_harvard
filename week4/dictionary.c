// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#include "dictionary.h"

// Represents number of children for each node in a trie
#define N 27
// Represents a node in a trie
typedef struct node
{
    bool is_word;
    struct node *children[N];
}
node;

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

int _get_char_idx (char c);

// Represents a trie
node *root;
int word_count = 0;

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Initialize trie
    root = malloc(sizeof(node));
    if (root == NULL)
    {
        return false;
    }
    root->is_word = false;
    for (int i = 0; i < N; i++)
    {
        root->children[i] = NULL;
    }

    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];

    // Insert words into trie
    while (fscanf(file, "%s", word) != EOF)
    {
        int len = strlen(word);
        if (len > LENGTH || len < 1) {
            continue;
        }
        node* tmp = root;
        char* w = word;
        while (*w) {
            int letter_index = _get_char_idx(*w);
            if (tmp->children[letter_index] == NULL) {
                node* new_letter = _make_node();
                if (new_letter == NULL) {
                    printf("out of memory");
                    break;
                }
                tmp->children[letter_index] = new_letter;
                tmp = new_letter;
            } else {
                tmp = tmp->children[letter_index];
            }
            w++;
        }
        tmp->is_word = 1;
        word_count++;
    }
    // Close dictionary
    fclose(file);
    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return word_count;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    if (root == NULL) {
        return false;
    }
    node* tmp = root;
    while (*word) {
        int letter_index = _get_char_idx(*word);
        tmp = tmp->children[letter_index];
        if(tmp == NULL) {
            return false;
        }
        word++;
    }
    return tmp->is_word == 1; // found, check if its a word
}

bool _destroy (node* current_node) {
    if (current_node == NULL) {
        return false;
    }
    for (int i = 0; i < N; i++) {
        _destroy(current_node->children[i]);
    }
    free(current_node);
    return true;

}
int _get_char_idx (char ch) {
    int letter_index = ch - 'a';
    if (isupper(ch)) {
        letter_index = ch - 'A';
    }else if (ch == '\'') {
        letter_index = 26;
    }
    return letter_index;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    return _destroy(root);
}