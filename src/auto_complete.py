'''
You need to design an autocomplete system for a search engine that suggests sentences as users type. The system works with the following specifications:

Initial Setup:

You're given an array of sentences and an array of times (both of length n)
sentences[i] represents a previously typed sentence
times[i] represents how many times that sentence was typed
How the System Works:

Users input characters one by one to form a sentence
Each sentence ends with the special character '#'
For each character typed (except '#'), the system returns the top 3 most frequent sentences that start with the prefix typed so far
Ranking Rules:

Sentences are ranked by their "hot degree" (frequency of being typed)
Higher frequency sentences appear first
If two sentences have the same frequency, they're sorted in ASCII order (lexicographically)
If fewer than 3 matching sentences exist, return all available matches
Special Behavior:

When '#' is input, it means the current sentence is complete
The completed sentence is added to the system (increasing its count by 1 if it already exists)
After '#' is input, return an empty list and reset for the next sentence
Implementation Requirements:

The AutocompleteSystem class needs two methods:

AutocompleteSystem(sentences, times): Constructor that initializes the system with historical data
input(c): Processes a single character input
If c == '#': saves the current sentence and returns []
Otherwise: returns a list of up to 3 sentence suggestions based on the current prefix
Example Flow: If a user types "i" then " " then "a", the system would:

After "i": return top 3 sentences starting with "i"
After "i ": return top 3 sentences starting with "i "
After "i a": return top 3 sentences starting with "i a"
After "i a#": save "i a" to the system and return []
'''
from __future__ import annotations
from typing import Dict, List, Optional

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]) -> None:
        self.freq_map: Dict[str, int] = dict(zip(sentences, times))
        self.current = []
        self.matches = []

    def input(self, c) -> List[str]:
        if c == '#':
            self.add_sentence()
            self.current = []
            self.matches = []
            return self.matches

        self.current.append(c)
        current_prefix = "".join(self.current)
        self.matches = [s for s in self.freq_map.keys() if s.startswith(current_prefix)]
        self.matches.sort(key=lambda s: (-self.freq_map[s], s))
        return self.matches[:3]

    def add_sentence(self):
        new_sent = "".join(self.current)
        self.freq_map[new_sent] = self.freq_map.get(new_sent, 0) + 1


class TrieNode:

    def __init__(self) -> None:
        self.children: List[Optional[TrieNode]] = [None]*27
        self.frequency: int = 0
        self.sentence: str = ''

    def insert(self, diff_sen: str, count: int):
        current_node: Optional[TrieNode] = self
        for char in diff_sen:
            index = 26 if char == ' ' else ord(char) - ord('a')
            if current_node.children[index] is None:
                current_node.children[index] = TrieNode()
                current_node.children[index].sentence = current_node.sentence+char
            current_node = current_node.children[index]
        current_node.frequency += count

    def search(self, prefix: str) -> Optional[TrieNode]:
        current_node: Optional[TrieNode] = self
        for char in prefix:
            index = 26 if char == ' ' else ord(char) - ord('a')
            if current_node.children[index] is None:
                return None
            else:
                current_node = current_node.children[index]
        return current_node


class AutocompleteSystemTree:

    def __init__(self, sentences: List[str], times: List[int]) -> None:
        self.root: TrieNode = TrieNode()
        for s, time in zip(sentences, times):
            self.root.insert(s, time)
        self.current_input: List[str] = []
        self.current_node: Optional[TrieNode] = self.root

    def input(self, char: str) -> List[str]:
        if char == '#':
            self.current_node.insert('', 1)
            self.current_input = []
            self.current_node = self.root
            return []
        self.current_input.append(char)
        self.current_node = self.current_node.search(char)
        result = []
        self._collect_all_sentances(self.current_node, result)
        result.sort(key=lambda t: (-t[1], t[0]))

        return [t[0] for t in result][:3]

    def _collect_all_sentances(self, node: Optional[TrieNode], all_sentences: List[tuple[str, int]]) -> None:
        if node is None:
            return
        if node.frequency > 0:
            all_sentences.append((node.sentence, node.frequency))
        for child_node in node.children:
            self._collect_all_sentances(child_node, all_sentences)
