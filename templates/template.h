// Auto-generated Solar Terms: $start_year to $end_year
#pragma once
#include <stdint.h>
#include <stddef.h>

const size_t SOLAR_TERMS_DATA_LENGTH = $data_length;

// Array of UNIX Epochs (UTC)
const uint32_t SOLAR_TERMS_TIMESTAMPS[] = {
    $epochs
};

// Array of corresponding Solar Term IDs (0-23)
const uint8_t SOLAR_TERMS_TERMS[] = {
    $terms
};

// Array of Solar Term English Names (Index 0-23)
const char* const SOLAR_TERMS_TERM_NAMES[] = {
    $term_names
};