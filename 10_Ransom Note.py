def canConstruct(ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for char in ransomNote:
            if char in magazine:
                magazine = magazine.replace(str(char), '' , 1)
            else:
                return False
        return True