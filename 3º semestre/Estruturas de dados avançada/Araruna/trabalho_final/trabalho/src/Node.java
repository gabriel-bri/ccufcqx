public class Node {
    public int key;
    public int height;
    public Node left;
    public Node right;
    
    public Node(int key) {
        this.key = key;
        this.height = 1;
        this.left = null;
        this.right = null;
    }
}