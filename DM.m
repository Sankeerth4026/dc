Fs = 500;                      
t = 0:1/Fs:1;                  
x = sin(2*pi*5*t);             
delta = 0.1;

e = zeros(size(t));
y = 0;

for i = 2:length(t)
    if x(i) > y
        e(i) = 1;  y = y + delta;
    else
        e(i) = 0;  y = y - delta;
    end
end

figure;
subplot(2,1,1); plot(t,x); title('Original Signal'); grid on;
subplot(2,1,2); stairs(t,e); title('Delta Encoded Signal'); grid on;