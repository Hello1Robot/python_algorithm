import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class Solution {


	private static class Tree {
		public Tree left;
		public Tree right;
		public int x;
		public int y;
		public int index;

		private Tree(int index, int x, int y){
			this.index = index;
			this.x = x;
			this.y = y;
		}
	}

	private void insert(Tree root, Tree tree){
		if(tree.x < root.x) {
			if (root.left == null) {
				root.left = tree;
			} else {
				insert(root.left, tree);
			}
		}else{
			if(root.right == null){
				root.right = tree;
			}else{
				insert(root.right, tree);
			}
		}

	}

	private Tree constructTree(Tree[] trees){
		Tree root = trees[0];
		for (int i = 1; i < trees.length; i++) {
			insert(root, trees[i]);
		}
		return root;
	}

	private void preOrder(Tree tree, List<Integer> result){
		if(tree == null) return;

		result.add(tree.index);
		preOrder(tree.left, result);
		preOrder(tree.right, result);
	}
	private void postOrder(Tree tree, List<Integer> result){
		if(tree == null) return;
		postOrder(tree.left, result);
		postOrder(tree.right, result);
		result.add(tree.index);
	}

	public int[][] solution(int[][] nodeinfo) {

		int n = nodeinfo.length;
		Tree[] trees = new Tree[n];
		for (int i = 0; i < n; i++) {
			trees[i] = new Tree(i+1, nodeinfo[i][0], nodeinfo[i][1]);
		}
		Arrays.sort(trees, (a, b) -> b.y - a.y);

		Tree root = constructTree(trees);

		List<Integer> pre = new ArrayList<>();
		List<Integer> post = new ArrayList<>();

		preOrder(root, pre);
		postOrder(root, post);




		return new int[][]{
			pre.stream().mapToInt(Integer::intValue).toArray(),
			post.stream().mapToInt(Integer::intValue).toArray()
		};
	}
}