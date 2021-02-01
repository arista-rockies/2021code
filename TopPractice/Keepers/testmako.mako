

%for key, val in test1.items():
    ${key} is ${val}
%endfor

%for item in test2:
    interface ethernet ${item}
%endfor