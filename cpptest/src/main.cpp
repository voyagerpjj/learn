#include <stdio.h>
#define N 20
#define S 100
int a;
double pin() //平均数
{
  double c = 0;
  int nums[N] = {1, 3, 7, 9, 4, 10};
  int b, i, j, temp;
  // for(i = 0 ; i < a ; i++)
  // {
  // 	scanf("%d",&b);
  // 	nums[i] = b;
  // }

  for (i = 0; i < a; i++) {
    for (j = 0; j < a - i - 1; j++) {
      if (nums[j] < nums[j + 1]) {
        temp = nums[j];
        nums[j] = nums[j + 1];
        nums[j + 1] = temp;
      }
    }
  }                       //冒泡排序
  for (i = 0; i < a; i++) //替换
  {
    nums[i] = nums[i + 1];
  }
  for (i = 0; i < a - 2; i++) //加
  {
    c += nums[i];
  }
  c = c / (double)(a - 2);
  return c;
}
int main_1() {
  double num[S];
  int d, e, f, k, i, j, temp1;
  scanf("%d", &d); //输入人数
  scanf("%d", &a); //输入评委数
  for (k = 0; k < d; k++) {
    double f = pin();
    num[k] = f;
  }

  for (i = 0; i < d; i++) {
    for (j = 0; j < d - i; j++) {
      if (num[j] < num[j + 1]) {
        temp1 = num[j];
        num[j] = num[j + 1];
        num[j + 1] = temp1;
      }
    }
  } //冒泡排序
  printf("%.2lf", num[0]);
  return 0;
}
