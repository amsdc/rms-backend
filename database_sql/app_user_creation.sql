-- Insert sample data
INSERT INTO users (username, password, user_type) VALUES ("__system", "", "admin"); -- future use
INSERT INTO users (username, password, user_type) VALUES ("default", "pbkdf2:sha256:260000$fstVNUjfKcKNVoH4$35cf1b3d453e80440b63cd09560d570d87606cbcf0ce3d38504c520d289add1e", "manager");