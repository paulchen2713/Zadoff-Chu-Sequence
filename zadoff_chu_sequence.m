% 
% zadoff_chu_sequence() Generate a Zadoff-Chu sequence.
% 
function y = zadoff_chu_sequence(N, R, Q)
    %
    %   y = zadoff_chu_sequence(N, R, Q) returns a Zadoff-Chu sequence of length N,
    %   with root index R, and cyclic shift Q.
    %
    %   The sequence is defined as:
    %       y(n) = exp(-1j * pi * R * n * (n + cf + 2 * Q) / N)
    %   where n = 0, 1, ..., N-1, and cf = mod(N, 2).
    %
    %   Inputs:
    %       N - Sequence length (positive integer)
    %       R - Root index (integer satisfying gcd(N, R) == 1)
    %       Q - Cyclic shift (integer, default is 0)
    %
    %   Output:
    %       y - Generated Zadoff-Chu sequence (complex column vector)
    %
    %   Example:
    %       N = 63;
    %       R = 5;
    %       Q = 0;
    %       y = zadoff_chu_sequence(N, R, Q);
    %
    %   References:
    %       3GPP TS 36.211 - Physical Channels and Modulation
    
    % Set default value for Q if not provided
    if nargin < 3
        Q = 0;
    end

    % Input validation
    if ~isscalar(N) || ~isnumeric(N) || N <= 0 || floor(N) ~= N
        error('N must be a positive integer.');
    end

    if ~isscalar(R) || ~isnumeric(R) || floor(R) ~= R
        error('R must be an integer.');
    end

    if ~isscalar(Q) || ~isnumeric(Q) || floor(Q) ~= Q
        error('Q must be an integer.');
    end

    % Check if N and R are coprime
    if gcd(N, R) ~= 1
        error('ZC sequence length N and parameter R must be coprime. %d and %d are not coprime.', N, R);
    end

    % Determine whether N is even or odd (cf = conjugate flag)
    cf = mod(N, 2); % cf = 0 for even N, cf = 1 for odd N

    % Generate sequence indices
    n = (0:N-1).'; % Column vector for consistency

    % Calculate the exponent for the Zadoff-Chu sequence
    exponent = -1j * pi * R * n .* (n + cf + 2 * Q) / N;

    % Generate the Zadoff-Chu sequence
    y = exp(exponent);
end
    