import java.util.*;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        System.out.println("Hello, World!");
        // 快速排序示例
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        System.out.println("排序前的数组:");
        printArray(arr);
        quickSort(arr, 0, arr.length-1);
        System.out.println("排序后的数组:");
        printArray(arr);
    }

    // 打印数组的辅助方法
    private static void printArray(int[] arr) {
        for (int i : arr) {
            System.out.print(i + " ");
        }
        System.out.println();
    }

    // 快速排序的主要方法
    private static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    // 分区方法
    private static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = (low - 1);
        
        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                // 交换 arr[i] 和 arr[j]
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        
        // 交换 arr[i+1] 和 arr[high] (pivot)
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        
        return i + 1;
    }
}
