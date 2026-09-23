#include <stdio.h>
#include <stdlib.h>

int cmp(const void* a, const void* b) {
    long diff = (long)*(int*)a - (long)*(int*)b;
    if (diff > 0) return 1;
    if (diff < 0) return -1;
    return 0;
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** fourSum(int* nums, int numsSize, int target, int* returnSize, int** returnColumnSizes) {
    *returnSize = 0;
    if (numsSize < 4) {
        *returnColumnSizes = NULL;
        return NULL;
    }

    // Array sort karna
    qsort(nums, numsSize, sizeof(int), cmp);

    int capacity = 1000;
    int** result = (int**)malloc(sizeof(int*) * capacity);
    *returnColumnSizes = (int*)malloc(sizeof(int) * capacity);

    for (int i = 0; i < numsSize - 3; i++) {
        // First element ke duplicates skip karna
        if (i > 0 && nums[i] == nums[i - 1]) continue;

        for (int j = i + 1; j < numsSize - 2; j++) {
            // Second element ke duplicates skip karna
            if (j > i + 1 && nums[j] == nums[j - 1]) continue;

            int left = j + 1;
            int right = numsSize - 1;

            while (left < right) {
                // Integer overflow se bachne ke liye long long use kiya gaya hai
                long long sum = (long long)nums[i] + nums[j] + nums[left] + nums[right];

                if (sum == target) {
                    if (*returnSize >= capacity) {
                        capacity *= 2;
                        result = (int**)realloc(result, sizeof(int*) * capacity);
                        *returnColumnSizes = (int*)realloc(*returnColumnSizes, sizeof(int) * capacity);
                    }

                    result[*returnSize] = (int*)malloc(sizeof(int) * 4);
                    result[*returnSize][0] = nums[i];
                    result[*returnSize][1] = nums[j];
                    result[*returnSize][2] = nums[left];
                    result[*returnSize][3] = nums[right];
                    (*returnColumnSizes)[*returnSize] = 4;
                    (*returnSize)++;

                    // Third aur fourth element ke duplicates skip karna
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;

                    left++;
                    right--;
                } else if (sum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }
    }

    return result;
}