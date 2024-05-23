#include <iostream>
#include <limits>
using namespace std;

struct AVLNode {
    long long value;
    AVLNode* left;
    AVLNode* right;
    int height;

    AVLNode(long long val) : value(val), left(nullptr), right(nullptr), height(1) {}
};

class AVLTree {
private:
    AVLNode* root;

    int getHeight(AVLNode* node) {
        return node ? node->height : 0;
    }

    int getBalance(AVLNode* node) {
        return node ? getHeight(node->left) - getHeight(node->right) : 0;
    }

    void updateHeight(AVLNode* node) {
        if (node) {
            node->height = 1 + max(getHeight(node->left), getHeight(node->right));
        }
    }

    AVLNode* rotateRight(AVLNode* y) {
        AVLNode* x = y->left;
        AVLNode* T2 = x->right;

        x->right = y;
        y->left = T2;

        updateHeight(y);
        updateHeight(x);

        return x;
    }

    AVLNode* rotateLeft(AVLNode* x) {
        AVLNode* y = x->right;
        AVLNode* T2 = y->left;

        y->left = x;
        x->right = T2;

        updateHeight(x);
        updateHeight(y);

        return y;
    }

    AVLNode* insert(AVLNode* node, long long value) {
        if (!node) return new AVLNode(value);

        if (value < node->value) {
            node->left = insert(node->left, value);
        } else if (value > node->value) {
            node->right = insert(node->right, value);
        } else {
            return node;
        }

        updateHeight(node);
        int balance = getBalance(node);

        if (balance > 1 && value < node->left->value) {
            return rotateRight(node);
        }

        if (balance < -1 && value > node->right->value) {
            return rotateLeft(node);
        }

        if (balance > 1 && value > node->left->value) {
            node->left = rotateLeft(node->left);
            return rotateRight(node);
        }

        if (balance < -1 && value < node->right->value) {
            node->right = rotateRight(node->right);
            return rotateLeft(node);
        }

        return node;
    }

    AVLNode* findMin(AVLNode* node) {
        AVLNode* current = node;
        while (current->left) current = current->left;
        return current;
    }

    AVLNode* deleteNode(AVLNode* root, long long value, bool &deleted) {
        if (!root) {
            deleted = false;
            return root;
        }

        if (value < root->value) {
            root->left = deleteNode(root->left, value, deleted);
        } else if (value > root->value) {
            root->right = deleteNode(root->right, value, deleted);
        } else {
            deleted = true;
            if (!root->left || !root->right) {
                AVLNode* temp = root->left ? root->left : root->right;

                if (!temp) {
                    temp = root;
                    root = nullptr;
                } else {
                    *root = *temp;
                }
                delete temp;
            } else {
                AVLNode* temp = findMin(root->right);
                root->value = temp->value;
                root->right = deleteNode(root->right, temp->value, deleted);
            }
        }

        if (!root) return root;

        updateHeight(root);
        int balance = getBalance(root);

        if (balance > 1 && getBalance(root->left) >= 0) {
            return rotateRight(root);
        }

        if (balance > 1 && getBalance(root->left) < 0) {
            root->left = rotateLeft(root->left);
            return rotateRight(root);
        }

        if (balance < -1 && getBalance(root->right) <= 0) {
            return rotateLeft(root);
        }

        if (balance < -1 && getBalance(root->right) > 0) {
            root->right = rotateRight(root->right);
            return rotateLeft(root);
        }

        return root;
    }

    AVLNode* upper(AVLNode* root, long long x) {
        AVLNode* result = nullptr;
        while (root) {
            if (root->value >= x) {
                result = root;
                root = root->left;
            } else {
                root = root->right;
            }
        }
        return result;
    }

    AVLNode* lower(AVLNode* root, long long x) {
        AVLNode* result = nullptr;
        while (root) {
            if (root->value <= x) {
                result = root;
                root = root->right;
            } else {
                root = root->left;
            }
        }
        return result;
    }

public:
    AVLTree() : root(nullptr) {}

    void insert(long long value) {
        root = insert(root, value);
    }

    string deleteNode(long long value) {
        bool deleted = false;
        root = deleteNode(root, value, deleted);
        return deleted ? "OK" : "BRAK";
    }

    string upper(long long x) {
        AVLNode* node = upper(root, x);
        return node ? to_string(node->value) : "BRAK";
    }

    string lower(long long x) {
        AVLNode* node = lower(root, x);
        return node ? to_string(node->value) : "BRAK";
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    AVLTree tree;

    for (int i = 0; i < N; ++i) {
        char operation;
        long long x;
        cin >> operation >> x;

        switch (operation) {
            case 'I':
                tree.insert(x);
                break;
            case 'D':
                cout << tree.deleteNode(x) << '\n';
                break;
            case 'U':
                cout << tree.upper(x) << '\n';
                break;
            case 'L':
                cout << tree.lower(x) << '\n';
                break;
        }
    }

    return 0;
}

