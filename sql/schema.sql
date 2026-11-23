-- 1. Electives table
CREATE TABLE IF NOT EXISTS electives (
    elective_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    course_code VARCHAR(30) UNIQUE NOT NULL,
    course_name VARCHAR(150) NOT NULL,
    credit_hours NUMERIC(3,1),
    department VARCHAR(100),
    prerequisites TEXT[],
    semester SMALLINT,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);


-- 2. Student results table
CREATE TABLE IF NOT EXISTS student_results (
    result_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    session_id VARCHAR(100) NOT NULL,
    subject_name VARCHAR(150) NOT NULL,
    marks NUMERIC(5,2),
    grade VARCHAR(5),
    credit_hours NUMERIC(3,1),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);


-- 3. Recommendations table
CREATE TABLE IF NOT EXISTS recommendations (
    recommendation_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    session_id VARCHAR(100) NOT NULL,
    elective_id BIGINT REFERENCES electives(elective_id)
        ON DELETE CASCADE,
    score NUMERIC(5,2),
    explanation TEXT,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);


-- 4. Answer cache table
CREATE TABLE IF NOT EXISTS answer_cache (
    cache_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    query_hash VARCHAR(64) UNIQUE NOT NULL,
    answer TEXT NOT NULL,
    source_metadata JSONB,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMPTZ
);



-- Create indexes for faster searches
CREATE INDEX IF NOT EXISTS idx_student_results_session
ON student_results(session_id);

CREATE INDEX IF NOT EXISTS idx_recommendations_session
ON recommendations(session_id);

CREATE INDEX IF NOT EXISTS idx_answer_cache_expiry
ON answer_cache(expires_at);