#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>      /* Ch 7: Standard Library Time functions */
#include <sys/types.h> /* Ch 8: System Types */
#include <sys/stat.h>  /* Ch 8: Stat structure for inodes */
#include <dirent.h>    /* Ch 8: Directory entries */

#define S_IFMT 0170000 /* Type of file mask */
#define S_IFDIR 0040000 /* Directory */


/* CHAPTER 6: Typedef and Structures */
typedef struct tnode
{
    char *path;         /* Pointer to file path string */
    off_t size;         /* File size (from stat) */
    time_t mtime;       /* Last modification time */
    struct tnode *left; /* Ch 6: Self-referential pointers */
    struct tnode *right;
} Treenode;

/* Function Prototypes */
void process_dir(char *name);
Treenode *addtree(Treenode *p, char *path, off_t size, time_t mtime);
void treeprint(Treenode *p);
void freetree(Treenode *p);
char *strdup_custom(char *s); /* Ch 6: Helper for string duplication */

/* Global root for the tree */
Treenode *root = NULL;

/* CHAPTER 5: Command-line Arguments */
int main(int argc, char *argv[])
{
    char *start_dir;

    /* Ch 5: Pointer arithmetic on argv */
    if (argc == 1)
        start_dir = ".";
    else
        start_dir = argv;

    printf("Scanning directory: %s\n", start_dir);
    process_dir(start_dir);

    printf("\n%-30s %-15s %s\n", "File Path", "Bytes", "Last Modified");
    printf("----------------------------------------------------------------\n");

    /* Ch 6: Recursive tree traversal */
    treeprint(root);
    freetree(root);

    return 0;
}

/* CHAPTER 8: UNIX System Interface (Directory Listing)
   Adapted from K&R Section 8.6 "fsize" */
void process_dir(char *dir)
{
    char name;
    struct dirent *dp;
    DIR *dfd;
    struct stat stbuf;

    /* Ch 8: opendir system call */
    if ((dfd = opendir(dir)) == NULL)
    {
        /* Ch 7: Error handling with stderr */
        fprintf(stderr, "error: can't open directory %s\n", dir);
        return;
    }

    /* Ch 8: readdir loop */
    while ((dp = readdir(dfd)) != NULL)
    {
        /* Ch 5: String comparison */
        if (strcmp(dp->d_name, ".") == 0 || strcmp(dp->d_name, "..") == 0)
            continue;

        /* Ch 7: Formatted string creation (sprintf) */
        if (strlen(dir) + strlen(dp->d_name) + 2 > sizeof(name))
            fprintf(stderr, "error: path name %s/%s too long\n", dir, dp->d_name);
        else
        {
            sprintf(name, "%s/%s", dir, dp->d_name);

            /* Ch 8: stat system call to get inode info */
            if (stat(name, &stbuf) == -1)
            {
                fprintf(stderr, "error: can't access %s\n", name);
                continue;
            }

            /* Ch 8: Bitwise masking to check file type modes */
            if ((stbuf.st_mode & S_IFMT) == S_IFDIR)
            {
                process_dir(name); /* Recursive call for sub-directories */
            }
            else
            {
                /* Add regular files to our sort tree */
                root = addtree(root, name, stbuf.st_size, stbuf.st_mtime);
            }
        }
    }
    closedir(dfd);
}

/* CHAPTER 6: Dynamic Memory & Structures */
Treenode *talloc(void);

Treenode *addtree(Treenode *p, char *path, off_t size, time_t mtime)
{
    if (p == NULL)
    {
        p = talloc(); /* Ch 7/8: Dynamic Storage Allocation */
        p->path = strdup_custom(path);
        p->size = size;
        p->mtime = mtime;
        p->left = p->right = NULL;
    }
    else if (size < p->size)
    {
        /* Sort by SIZE, not name */
        p->left = addtree(p->left, path, size, mtime);
    }
    else
    {
        p->right = addtree(p->right, path, size, mtime);
    }
    return p;
}

/* CHAPTER 7: Formatted Output */
void treeprint(Treenode *p)
{
    char timebuf;
    if (p != NULL)
    {
        treeprint(p->left); /* Print smaller files first */

        /* Ch 7: Date and Time Functions */
        struct tm *t_info = localtime(&p->mtime);
        strftime(timebuf, sizeof(timebuf), "%Y-%m-%d %H:%M", t_info);

        /* Ch 7: Variable field width printing */
        printf("%-30.30s %-15ld %s\n", p->path, (long)p->size, timebuf);

        treeprint(p->right);
    }
}

/* CHAPTER 8: Storage Allocator Wrapper */
Treenode *talloc(void)
{
    /* Ch 7: malloc requires a cast and sizeof */
    return (Treenode *)malloc(sizeof(Treenode));
}

char *strdup_custom(char *s)
{
    char *p;
    /* Ch 5: String length + 1 for null terminator */
    p = (char *)malloc(strlen(s) + 1);
    if (p != NULL)
        strcpy(p, s);
    return p;
}

/* Memory cleanup */
void freetree(Treenode *p)
{
    if (p != NULL)
    {
        freetree(p->left);
        freetree(p->right);
        free(p->path); /* Ch 7: free() */
        free(p);
    }
}
