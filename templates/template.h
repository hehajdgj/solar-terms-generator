#ifndef AUTO_GENERATED_SOLAR_TERMS_H
#define AUTO_GENERATED_SOLAR_TERMS_H

// Auto-generated Solar Terms: $start_year to $end_year
#pragma once
#include <array>
#include <cstddef>
#include <cstdint>

constexpr size_t SOLAR_TERMS_DATA_LENGTH = $data_length;

// Array of UNIX Epochs (UTC)
constexpr std::array<int64_t, $data_length> SOLAR_TERMS_TIMESTAMPS = {$epochs};

// Array of corresponding Solar Term IDs (0-23)
constexpr std::array<uint8_t, $data_length> SOLAR_TERMS_TERMS = {$terms};

// Enum of Solar Terms
enum class SolarTermName : uint8_t {
$term_names
};

#endif // AUTO_GENERATED_SOLAR_TERMS_H