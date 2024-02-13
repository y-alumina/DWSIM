% Parameter simulasi
flow_in = 0.5;  % Laju aliran masuk
C_in = 2.0;  % Konsentrasi masuk
flow_out = 0.2;  % Laju aliran keluar
V = 10.0;    % Volume tangki
waktu_simulasi = 100.0;  % Waktu simulasi
delta_t = 1.0;  % Langkah waktu simulasi

% Jalankan simulasi
hasil_simulasi = tangki_reaktor(flow_in, C_in, flow_out, V, waktu_simulasi, delta_t);

% Plot hasil simulasi
plot_simulasi(hasil_simulasi);

function hasil_simulasi = tangki_reaktor(flow_in, C_in, flow_out, V, waktu_simulasi, delta_t)
    % Inisialisasi variabel
    t = 0;
    C = 0.0;
    hasil_simulasi = [t, C]; % Initialize as a matrix with two columns

    % Equation
    while t < waktu_simulasi
        dCdt = (flow_in * (C_in - C) - flow_out * C) / V;
        C = C + delta_t * dCdt;
        t = t + delta_t;
        hasil_simulasi = [hasil_simulasi; [t, C]];
    end
end

function plot_simulasi(hasil_simulasi)
    % Ekstraksi data untuk plotting
    waktu = hasil_simulasi(:, 1);
    konsentrasi = hasil_simulasi(:, 2);

    % Plot hasil simulasi
    figure;
    plot(waktu, konsentrasi);
    xlabel('Waktu');
    ylabel('Konsentrasi');
    title('Simulasi Tangki Reaktor Kontinyu');
    grid on;
end
