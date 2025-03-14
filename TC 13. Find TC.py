'''What is the time complexity of the following code snippet'''

int func(int n){
  int s = 0;
  for(int i = 1 ; i*i*i <= n ; i++){
    s = s + i;
  }
  return s;
}

Options:
1. O(n ^ (1/4))
2. O(n ^ (1/3))
3. O(n ^ (1/2))
4. O(n)

Ans:
2
