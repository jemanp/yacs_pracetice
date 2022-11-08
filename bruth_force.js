function searchString(text, pattern) {
    let i = 0;
    while (i <= text.length - pattern.length) { //pattern should not be the length of text
        let p = 0; //p pointing the very first idx
        while (p < pattern.length) { //pattern should not be the length of text
            if (text[i + p] != pattern[p]) {//if text and pettern letters are not matched
                break; 
            }
            p = p + 1; //move the pointing pointer one idx
        }
        if (p === pattern.length) { //if pattern letters are matched with text                                    //if pattern letters are matched with text
            return i; //return the starting idx of matching text of idx
        }
        i = i + 1; //move the text idx to right
    }
    return -1;
}