function print_sequence(symbols)
    sz = size(symbols);
    for i = 1:sz(1)
        % symbol = cos(theta) + j*sin(theta) = r*e^{j*theta}
        symbol = real(symbols(i)) + 1j*imag(symbols(i));
        r = abs(symbol); theta = angle(symbol);
        fprintf('#%02d  % .4f + % .4fj, r = %.1f, theta = % .4f = % .1f\n', ...
            i, real(symbol), imag(symbol), r, theta, rad2deg(angle(symbol)));
    end
end
