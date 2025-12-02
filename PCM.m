clc; clear; close all;

% Inputs
n  = input('Enter n value for N-bit PCM system: ');
n1 = input('Enter number of samples in a period: ');
L  = 2^n; 

% Signals
t  = linspace(0,4*pi,1000);          % smooth analog
sA = 8*sin(t);
s  = 8*sin(linspace(0,4*pi,n1));     % sampled

% Quantization
del = 16/L;                          % (vmax-vmin)/L
q = zeros(size(s));
for i = 1:n1
    idx = min(max(floor((s(i)+8)/del),0),L-1);
    q(i) = -8 + (idx+0.5)*del;
end

% Plots
subplot(3,1,1); plot(sA,'LineWidth',1.4); title('Analog Signal'); grid on;
subplot(3,1,2); stem(s,'filled');        title('Sampled Signal'); grid on;
subplot(3,1,3); stem(q,'filled');        title('Quantized Signal'); grid on;