const leetcodeTasks = [
    {
      title: "Úloha 1: Two Sum",
      description: "Popis úlohy: Najděte dvě čísla v poli, jejichž součet je roven dané hodnotě target. Vráťte indexy těchto čísel. Každý vstup má přesně jedno řešení a není dovoleno použít stejné číslo dvakrát.",
      problemUrl: "https://leetcode.com/problems/two-sum/",
      solutionUrl: "https://github.com/Matty-Jaris/LeetCode-solutions/blob/main/1_two_sum"
    },
    {
      title: "Úloha 2: Palindrome Number",
      description: "Popis úlohy: Úloha spočívá v tom, zjistit, zda je dané celé číslo palindrom. Palindrom je číslo, které čte stejně zleva i zprava. Úkolem je vrátit hodnotu true, pokud je číslo palindrom, nebo false, pokud není.",
      problemUrl: "https://leetcode.com/problems/palindrome-number/",
      solutionUrl: "https://github.com/Matty-Jaris/LeetCode-solutions/blob/main/2_palindrome_number"
    },
    {
      title: "Úloha 3: Roman to Integer",
      description: "Popis úlohy: Úloha spočívá v převodu římského čísla na celé číslo. Římská čísla jsou tvořena kombinací symbolů, přičemž některé symboly, jako například I před V nebo X, znamenají odečítání. Cílem je správně interpretovat tuto kombinaci a převést ji na odpovídající hodnotu celého čísla.",
      problemUrl: "https://leetcode.com/problems/roman-to-integer/",
      solutionUrl: "https://github.com/Matty-Jaris/LeetCode-solutions/blob/main/3_roman_to_integer"
    },
    {
      title: "Úloha 4: Longest Common Prefix",
      description: "Úloha spočívá v nalezení nejdelšího společného prefixu mezi řetězci v poli. Pokud takový prefix neexistuje, vrátí se prázdný řetězec.",
      problemUrl: "https://leetcode.com/problems/longest-common-prefix/",
      solutionUrl: "https://github.com/Matty-Jaris/LeetCode-solutions/blob/main/4_longest_common_prefix"
    },
    {
      title: "Úloha 5: Valid Parentheses",
      description: "Úloha spočívá v ověření, zda je zadaný řetězec obsahující pouze závorky ('(', ')', '{', '}', '[' a ']') validní. Řetězec je validní, pokud je každá otevřená závorka uzavřena správným typem závorky a závorky jsou uzavřeny ve správném pořadí. Pokud všechny závorky v řetězci odpovídají těmto pravidlům, vrátí se true. Jinak se vrátí false.",
      problemUrl: "https://leetcode.com/problems/valid-parentheses/",
      solutionUrl: "https://github.com/Matty-Jaris/LeetCode-solutions/blob/main/5_valid_parentheses"
    },
    {
      title: "Úloha 6: Merge Two Sorted Lists",
      description: "Úkolem je sloučit dva seřazené spojové seznamy do jednoho seřazeného seznamu. Seznamy by měly být propojeny tak, že jejich uzly budou spojeny do jednoho nového seznamu, který bude mít prvky v seřazeném pořadí. Výsledkem je hlava nového sloučeného seznamu.",
      problemUrl: "https://leetcode.com/problems/merge-two-sorted-lists/",
      solutionUrl: "https://github.com/Matty-Jaris/LeetCode-solutions/blob/main/6_merge_two_sorted_lists"
    },
    {
      title: "Úloha 7: Remove Duplicates from Sorted Array",
      description: "Úkolem je odstranit duplicity z již seřazeného pole čísel tak, aby každé unikátní číslo bylo v poli pouze jednou, a zachovat původní pořadí. Funkce by měla upravit původní pole a vrátit počet unikátních prvků. Ostatní prvky po unikátních hodnotách jsou irelevantní.",
      problemUrl: "https://leetcode.com/problems/remove-duplicates-from-sorted-array/",
      solutionUrl: "https://github.com/Matty-Jaris/LeetCode-solutions/blob/main/7_remove_duplicates_from_sorted_array"
    },
    {
      title: "Úloha 8: Remove Element",
      description: "Úkolem je odstranit všechny výskyty dané hodnoty z pole čísel tak, že zbytek pole bude obsahovat pouze hodnoty, které nejsou rovny dané hodnotě. Po provedení úpravy by funkce měla vrátit počet prvků, které nejsou rovny dané hodnotě. Zbytek pole je irelevantní a není nutné ho upravovat.",
      problemUrl: "https://leetcode.com/problems/remove-element/",
      solutionUrl: "https://github.com/Matty-Jaris/LeetCode-solutions/blob/main/8_remove_element"
    },
    {
      title: "Úloha 9: Find the Index of the First Occurrence in a String",
      description: "Úloha spočívá v nalezení prvního výskytu podřetězce (needle) v řetězci (haystack). Pokud je podřetězec přítomen, vrátíme index jeho prvního výskytu. Pokud není podřetězec součástí řetězce, vrátíme -1.",
      problemUrl: "https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/",
      solutionUrl: "https://github.com/Matty-Jaris/LeetCode-solutions/blob/main/9_find_the_index_of_the_first_occurrence_in_a_string"
    },
    {
      title: "Úloha 10: Search Insert Position",
      description: "Úkolem je najít index, na kterém by měl být vložen cílový prvek v seřazeném poli celých čísel. Pokud je prvek již v poli, vrátíme jeho index. Pokud není, vrátíme index, kde by měl být vložen, aby pole zůstalo seřazeno. Algoritmus musí běžet v čase O(log n), což naznačuje použití binárního vyhledávání.",
      problemUrl: "https://leetcode.com/problems/search-insert-position/",
      solutionUrl: "https://github.com/Matty-Jaris/LeetCode-solutions/blob/main/10_search_insert_position"
    },    
  
  ];