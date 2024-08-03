int reverse(int x){
    long int s=0;
    while(x!=0){
        if(s>INT_MAX/10 || s<INT_MIN/10)
            return 0;
        s=s*10+x%10;
        x/=10;
    }
    printf("%d",s);
    return s;
}

// if (s > INT_MAX / 10 || s < INT_MIN / 10)
// This condition checks two scenarios:
// a) s > INT_MAX / 10: This checks if s is greater than one-tenth of the 
// maximum possible integer value. If it is, multiplying s by 10 in the 
// next step would cause an overflow.
// b) s < INT_MIN / 10: Similarly, this checks if s is less than one-tenth 
// of the minimum possible integer value. If it is, multiplying s by 10 
// could cause an underflow for negative numbers.