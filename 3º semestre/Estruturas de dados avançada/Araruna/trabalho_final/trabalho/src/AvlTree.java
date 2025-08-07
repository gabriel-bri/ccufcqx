    public class AvlTree extends AVLMetodos {
        private Node root = null;

        public AvlTree() {
            // Construtor padrão
        }

        // Retorna a altura do nó.
        // Se a árvore for vazia ela tem altura 0
        // Caso contrário, retorna o valor que está no campo height
        private int height(Node node) {
            return (node == null) ? 0 : node.height;
        }

        private int balance(Node node) {
            return height(node.right) - height(node.left);
        }

        private Node rightRotation(Node p) {
            Node u = p.left;
            p.left = u.right;
            u.right = p;
            // Recalcular as alturas de p e de u
            p.height = 1 + Math.max(height(p.left), height(p.right));
            u.height = 1 + Math.max(height(u.left), height(u.right));
            return u;
        }

        private Node leftRotation(Node p) {
            Node u = p.right;
            p.right = u.left;
            u.left = p;
            // Recalcular as alturas de p e de u
            p.height = 1 + Math.max(height(p.right), height(p.left));
            u.height = 1 + Math.max(height(u.left), height(u.right));
            return u;
        }

        // Função pública que recebe uma chave e a insere
        // somente se ela não for repetida
        @Override
        public void add(int key) {
            root = add(root, key);
        }

        // Função recursiva privada que recebe uma raiz de arvore
        // e uma chave e insere a chave na tree se e somente se 
        // ela nao for repetida. Claro, tem que deixar AVL novamente
        private Node add(Node p, int key) {
            if (p == null)
                return new Node(key);
            if (key == p.key)
                return p;
            if (key < p.key)
                p.left = add(p.left, key);
            else
                p.right = add(p.right, key);

            p = fixup_node(p, key);

            return p;
        }

        private Node fixup_node(Node p, int key) {
            // Recalcula a altura de p
            p.height = 1 + Math.max(height(p.left), height(p.right));

            // Calcula o balanço do p
            int bal = balance(p);

            if (bal >= -1 && bal <= 1) {
                return p;
            }

            if (bal < -1 && key < p.left.key) {
                System.out.println("Rotação simples à direita (LL) no nó " + p.key);
                p = rightRotation(p);
            } else if (bal < -1 && key > p.left.key) {
                System.out.println("Rotação dupla à direita (LR) no nó " + p.key);
                p.left = leftRotation(p.left);
                p = rightRotation(p);
            } else if (bal > 1 && key > p.right.key) {
                System.out.println("Rotação simples à esquerda (RR) no nó " + p.key);
                p = leftRotation(p);
            } else if (bal > 1 && key < p.right.key) {
                System.out.println("Rotação dupla à esquerda (RL) no nó " + p.key);
                p.right = rightRotation(p.right);
                p = leftRotation(p);
            }

            return p;
        }

        @Override
        public void clear() {
            root = clear(root);
        }

        private Node clear(Node node) {
            if (node != null) {
                node.left = clear(node.left);
                node.right = clear(node.right);
            }
            return null;
        }

        public void bshow() {
            bshow(root, "");
        }

        private void bshow(Node node, String heranca) {
            if (node != null && (node.left != null || node.right != null))
                bshow(node.right, heranca + "r");
            for (int i = 0; i < heranca.length() - 1; i++)
                System.out.print(heranca.charAt(i) != heranca.charAt(i + 1) ? "│   " : "    ");
            if (!heranca.equals(""))
                System.out.print(heranca.charAt(heranca.length() - 1) == 'r' ? "┌───" : "└───");
            if (node == null) {
                System.out.println("#");
                return;
            }
            System.out.println(node.key + " (B=" + balance(node) + ")");

            if (node != null && (node.left != null || node.right != null))
                bshow(node.left, heranca + "l");
        }

        @Override
        public boolean remove(int key) {
            BooleanWrapper found = new BooleanWrapper(false);
            root = remove(root, key, found);
            return found.value;
        }

        @Override
        public boolean empty() {
            return root == null;
        }

        @Override
        public boolean contains(int key) {
            Node current = root;
            while (current != null) {
                if (key == current.key)
                    return true;
                if (key < current.key)
                    current = current.left;
                else
                    current = current.right;
            }
            return false;
        }

        public void search_path(int key) {
            Node current = root;
            System.out.print("Caminho até a chave " + key + ": ");
            while (current != null) {
                if (key == current.key) {
                    System.out.println("{" + key + "}" + " | [OK] Chave encontrada!");
                    return;
                }
                System.out.print(current.key);
                System.out.print(" => ");
                if (key < current.key)
                    current = current.left;
                else
                    current = current.right;
            }
            System.out.println("[X] Chave não encontrada!");
        }

        // Versão privada
        private Node remove(Node node, int key, BooleanWrapper found) {
            if (node == null)
                return null;
            if (key < node.key)
                node.left = remove(node.left, key, found);
            else if (key > node.key)
                node.right = remove(node.right, key, found);
            else {
                found.value = true;
                if (node.right == null) {
                    Node child = node.left;
                    return child;
                } else {
                    node.right = remove_successor(node, node.right);
                }
            }

            node = fixup_deletion(node);
            return node;
        }

        private Node remove_successor(Node root, Node node) {
            if (node.left != null)
                node.left = remove_successor(root, node.left);
            else {
                root.key = node.key;
                Node aux = node.right;
                return aux;
            }
            // Atualiza a altura do node e regula o node
            node = fixup_deletion(node);
            return node;
        }

        private Node fixup_deletion(Node node) {
            node.height = 1 + Math.max(height(node.left), height(node.right));

            int bal = balance(node);

            // node pode estar desregulado, há 4 casos a considerar
            if (bal > 1 && balance(node.right) >= 0) {
                System.out.println("Rotação simples à esquerda (RR) no nó " + node.key + " após remoção");
                return leftRotation(node);
            } else if (bal > 1 && balance(node.right) < 0) {
                System.out.println("Rotação dupla à esquerda (RL) no nó " + node.key + " após remoção");
                node.right = rightRotation(node.right);
                return leftRotation(node);
            } else if (bal < -1 && balance(node.left) <= 0) {
                System.out.println("Rotação simples à direita (LL) no nó " + node.key + " após remoção");
                return rightRotation(node);
            } else if (bal < -1 && balance(node.left) > 0) {
                System.out.println("Rotação dupla à direita (LR) no nó " + node.key + " após remoção");
                node.left = leftRotation(node.left);
                return rightRotation(node);
            }

            System.out.println("[OK] Nó " + node.key + " está balanceado após remoção (B=" + bal + ")");
            return node;
        }

        public int height() {
            return (root == null) ? 0 : root.height;
        }

        public static int height_rec(Node node) {
            if (node == null)
                return 0;
            else {
                node.height = 1 + Math.max(height_rec(node.left), height_rec(node.right));
                return node.height;
            }
        }

        // Classe auxiliar para simular passagem por referência de boolean
        private static class BooleanWrapper {
            public boolean value;
            
            public BooleanWrapper(boolean value) {
                this.value = value;
            }
        }
    }