#include <stdio.h>
#include <string.h>

int flen(FILE*);
int get_num(const char*);
int try_parse_nums(const char*);

// idx + 1 is number, no need for a struct
char* nums[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

int main()
{
    FILE* f = fopen("/home/justin/CLionProjects/advent-of-code/input", "r");
    if (f == NULL) return 1;

    int const l = flen(f);
    char lines[l - 1][256];
    int count = 0;
    while (fgets(lines[count], 256, f))
    {
        count++;
    }
    fclose(f);
    int nums[l - 1];
    for (int i = 0; i < l; ++i)
    {
        nums[i] = get_num(lines[i]);
    }
    int sum = 0;
    for (int i = 0; i < l; i++) sum += nums[i];
    printf("%d\n", sum);
}

int get_num(const char* line)
{
    int first = -1;
    int last = -1;
    char buffer[256];
    int bufidx = 0;
    for (int i = 0; i < strlen(line); i++)
    {
        if (line[i] == '\n') continue;
        int next = line[i] - '0';
        // check if char is a number within 0..9
        if (next < 0 || next > 9)
        {
            buffer[bufidx] = line[i];
            buffer[bufidx + 1] = '\0';
            bufidx++;
            next = try_parse_nums(buffer);
        } else
        {
            // clear buffer
            buffer[0] = '\0';
            bufidx = 0;
        }
        // must either be -1 if check_buf fails or a number in proper range
        if (next != -1)
        {
            if (first == -1)
            {
                first = next;
            }
            else
            {
                last = next;
            }
        }
    }
    if (last == -1) last = first;
    // printf("%s: %d, %d\n", line, first, last);
    return first * 10 + last;
}

int try_parse_nums(const char* buffer)
{
    int num_idx = 0;
    int num = -1;
    // printf("%s ", buffer);
    for (int j = 0; j < 9; j++)
    {
        const char *result = buffer;
        const char *new = result;
        while (new != NULL) {
            result = new;
            new = strstr(result, nums[j]);
            if (new != NULL) new++;
        }
        if (result != NULL)
        {
            // return j + 1;
            const int new_idx = result - buffer;
            // printf("%d: %d, %d: %d\n", num_idx, num, new_idx, j + 1);
            if (new_idx > num_idx)
            {
                num_idx = new_idx;
                num = j + 1;
            }
        }
    }
    return num;
}

// returns the length of a file
int flen(FILE* f)
{
    int count = 1;
    fseek(f, 0, SEEK_SET);
    for (char c = fgetc(f); c != EOF; c = fgetc(f))
    {
        if (c == '\n') count++;
    }
    fseek(f, 0, SEEK_SET);
    return count;
}
