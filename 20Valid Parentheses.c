int top=-1;
char stack[10000];

char pop(){
    if(top==-1) return '\0';
    return stack[top--];
}

void push(char t){
    if(top<10000-1) stack[++top]=t;
}

bool isValid(char* s) {
    top=-1;

    for(int i=0;s[i]!='\0';i++){
        if(s[i]=='('||s[i]=='{'||s[i]=='['){
            push(s[i]);
        }
        else {
            if(s[i]==')'||s[i]=='}'||s[i]==']'){
                char p = pop();
                if((s[i]==')' && p!='(') || 
                    (s[i]==']' && p!='[') || 
                    (s[i]=='}' && p!='{')){
                       return false; 
                }
            }
        }
    }
    
    return top==-1;
}