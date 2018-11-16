/*  This file contains implementation of recursive 
 *          preorder traversal of binary trees.
 * 
 *
 * Author: Athavan Kanagasabapathy (15-Nov-2018)
 * time comp: O(n)
 * space comp: O(n)
 */

#include <iostream>
#include <queue>

#if 0
/* tree node structure */
class Node{

    int data;
    Node *left;
    Node *right;


    //constructor
    Node(int value) : data(value), left(nullptr), right(NULL){
        /* do nothing */
    }

    //destructor
    ~Node(){
        delete left;
        delete right;
    }

    //insertleft
    Node* insert_left(int value){
        this->left = new Node(value);
        return this->left;

    }

    //insertright
    Node* insert_right(int value){
        this->right = new Node(value);
        return this->right;
    }
};
#endif
using namespace std;

struct binarytreenode{
    int data;
    struct binarytreenode *left;
    struct binarytreenode *right;

    //constructor
    binarytreenode (int value){
        data = value;
        left = NULL;
        right = NULL;
    }
};

binarytreenode *root = NULL;

/* this goes level by level from left to right child in each of the level */
void insert_to_binary_tree(binarytreenode **root, int value){

    binarytreenode *node = NULL;
    binarytreenode *trav = *root;
    queue<binarytreenode*> levelq;
    
    if(*root == NULL){
        node = new binarytreenode(value);
        if (node == NULL){
            cout << "No memory to allocate\n";
        }
        *root = node;
    } else {
        /* enque the root */
        levelq.push(*root);

        while(!levelq.empty()){

            binarytreenode *temp = levelq.front();

            levelq.pop();

            if(temp->left == NULL){
                node = new binarytreenode(value);
                temp->left = node;
                return;
            } else {
                levelq.push(temp->left);
            }
            
            if(temp->right == NULL){
                node = new binarytreenode(value);
                temp->right = node;
                return;
            } else {
                levelq.push(temp->right);
            }
        }
    }

    return;
}

void print_preorder_recursive(binarytreenode *root){

    if (root == NULL)
        return;

    cout << root->data;
    cout << endl;
    print_preorder_recursive(root->left);
    print_preorder_recursive(root->right);
    return;
}

/* Driver program                     */
/*                  1                 */
/*            2               3       */
/*       4        5       6         7 */
/*                                      */

int main(void){

    /* first generate a tree like above */
    insert_to_binary_tree(&root,1);
    insert_to_binary_tree(&root,2);
    insert_to_binary_tree(&root,3);
    insert_to_binary_tree(&root,4);
    insert_to_binary_tree(&root,5);
    insert_to_binary_tree(&root,6);
    insert_to_binary_tree(&root,7);

    /* print the tree */
    print_preorder_recursive(root);

    return 0;
}
