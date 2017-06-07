package Tree;

//œ»–Ú±È¿˙
public class Recursion {
	public static void scanNodes(TreeNode root){
		if(root!=null){
			System.out.println("this is node: "+root.val);
			scanNodes(root.left);
			System.out.println("node"+root.val+" finish scanning left");  
            scanNodes(root.right);  
            System.out.println("node"+root.val+" finish scanning right");  
		}
	}
	
	public static void main(String[] args) {
		TreeNode root = new TreeNode(1);
		TreeNode left1 = new TreeNode(2);
		TreeNode right1 = new TreeNode(3);
		TreeNode left2 = new TreeNode(4);
		TreeNode right2 = new TreeNode(5);
		TreeNode right3 = new TreeNode(6);
		//create one tree
		root.left = left1;
		root.right = right1;
		left1.left = left2;
		left1.right = right2;
		right1.right = right3;
		
		scanNodes(root);
			
		

	}

}
