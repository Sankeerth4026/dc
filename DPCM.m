clc; clear; close all;

% Inputs
Fs = input('Enter sampling frequency: ');
fm = input('Enter message signal frequency: ');
L  = input('Enter number of quantization levels: ');

% Message signal
t = 0:1/Fs:1-1/Fs;
s = sin(2*pi*fm*t);

% Quantizer
xmin = -1; xmax = 1;
step = (xmax-xmin)/L;
codebook = xmin:step:xmax-step;

% DPCM: predict → difference → quantize
qdiff = zeros(size(s));
prev = 0;

for n = 2:length(s)
    diff = s(n) - s(n-1);     % predictor = previous sample
    [~, idx] = min(abs(diff - codebook));
    qdiff(n) = codebook(idx);
end

% Plots
figure;
subplot(3,1,1); plot(t,s); title('Original Signal'); grid on;
subplot(3,1,2); stem(t,s,'filled'); title('Sampled Signal'); grid on;
subplot(3,1,3); stairs(t,qdiff); title('Quantized DPCM Difference'); grid on;