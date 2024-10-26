% Example parameters
N = 10;  % Sequence length
R = 7;   % Root index
Q = 1;   % Cyclic shift

% Generate the Zadoff-Chu sequence
zc_sequence = zadoff_chu_sequence(N, R, Q);
% display(zc_sequence);
print_sequence(zc_sequence);

% Plot the magnitude and phase of the sequence
figure;
subplot(2,1,1);print_sequence
stem(abs(zc_sequence));
title('Magnitude of Zadoff-Chu Sequence');
xlabel('n');
ylabel('|y(n)|');

subplot(2,1,2);
stem(angle(zc_sequence));
title('Phase of Zadoff-Chu Sequence');
xlabel('n');
ylabel('Phase(y(n))');
