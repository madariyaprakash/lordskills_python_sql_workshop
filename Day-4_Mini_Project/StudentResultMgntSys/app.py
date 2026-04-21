from flask import Flask, request, jsonify
from db import get_connection

app = Flask(__name__)


# ─────────────────────────────────────────────
# Helper: assign grade based on average marks
# ─────────────────────────────────────────────
def calculate_grade(avg):
    if avg >= 90:
        return "O"          # Outstanding
    elif avg >= 80:
        return "A+"
    elif avg >= 70:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"          # Fail


# ─────────────────────────────────────────────
# 1. ADD STUDENT
# POST /students
# Body: { name, roll_no, department, email }
# ─────────────────────────────────────────────
@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()

    required = ["name", "roll_no", "department", "email"]
    for field in required:
        if field not in data or not data[field].strip():
            return jsonify({"error": f"'{field}' is required"}), 400

    try:
        conn   = get_connection()
        cursor = conn.cursor()

        sql = """
            INSERT INTO students (name, roll_no, department, email)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, (
            data["name"].strip(),
            data["roll_no"].strip(),
            data["department"].strip(),
            data["email"].strip()
        ))
        conn.commit()
        student_id = cursor.lastrowid

        return jsonify({
            "message":    "Student added successfully",
            "student_id": student_id
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        cursor.close()
        conn.close()


# ─────────────────────────────────────────────
# 2. EDIT STUDENT
# PUT /students/<id>
# Body: any of { name, department, email }
# ─────────────────────────────────────────────
@app.route("/students/<int:student_id>", methods=["PUT"])
def edit_student(student_id):
    data = request.get_json()

    allowed_fields = ["name", "department", "email"]
    updates = {k: v for k, v in data.items() if k in allowed_fields}

    if not updates:
        return jsonify({"error": "No valid fields to update"}), 400

    try:
        conn   = get_connection()
        cursor = conn.cursor()

        set_clause = ", ".join([f"{k} = %s" for k in updates])
        values     = list(updates.values()) + [student_id]

        cursor.execute(
            f"UPDATE students SET {set_clause} WHERE id = %s",
            values
        )
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"error": "Student not found"}), 404

        return jsonify({"message": "Student updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        cursor.close()
        conn.close()


# ─────────────────────────────────────────────
# 3. DELETE STUDENT
# DELETE /students/<id>
# ─────────────────────────────────────────────
@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    try:
        conn   = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"error": "Student not found"}), 404

        return jsonify({"message": "Student deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        cursor.close()
        conn.close()


# ─────────────────────────────────────────────
# 4. SEARCH STUDENT BY ID
# GET /students/<id>
# ─────────────────────────────────────────────
@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    try:
        conn   = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
        student = cursor.fetchone()

        if not student:
            return jsonify({"error": "Student not found"}), 404

        return jsonify(student), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        cursor.close()
        conn.close()


# ─────────────────────────────────────────────
# 5. ADD MARKS
# POST /students/<id>/marks
# Body: { subject, marks }
# ─────────────────────────────────────────────
@app.route("/students/<int:student_id>/marks", methods=["POST"])
def add_marks(student_id):
    data = request.get_json()

    if "subject" not in data or "marks" not in data:
        return jsonify({"error": "'subject' and 'marks' are required"}), 400

    if not (0 <= int(data["marks"]) <= 100):
        return jsonify({"error": "Marks must be between 0 and 100"}), 400

    try:
        conn   = get_connection()
        cursor = conn.cursor()

        # Check student exists
        cursor.execute("SELECT id FROM students WHERE id = %s", (student_id,))
        if not cursor.fetchone():
            return jsonify({"error": "Student not found"}), 404

        cursor.execute(
            "INSERT INTO marks (student_id, subject, marks) VALUES (%s, %s, %s)",
            (student_id, data["subject"].strip(), int(data["marks"]))
        )
        conn.commit()

        return jsonify({"message": "Marks added successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        cursor.close()
        conn.close()


# ─────────────────────────────────────────────
# 6. GRADE STUDENT
# GET /students/<id>/grade
# Returns all subjects, avg, and grade
# ─────────────────────────────────────────────
@app.route("/students/<int:student_id>/grade", methods=["GET"])
def grade_student(student_id):
    try:
        conn   = get_connection()
        cursor = conn.cursor(dictionary=True)

        # Get student info
        cursor.execute("SELECT name, roll_no FROM students WHERE id = %s", (student_id,))
        student = cursor.fetchone()

        if not student:
            return jsonify({"error": "Student not found"}), 404

        # Get all marks
        cursor.execute(
            "SELECT subject, marks FROM marks WHERE student_id = %s",
            (student_id,)
        )
        marks_list = cursor.fetchall()

        if not marks_list:
            return jsonify({"error": "No marks found for this student"}), 404

        total   = sum(row["marks"] for row in marks_list)
        average = round(total / len(marks_list), 2)
        grade   = calculate_grade(average)

        return jsonify({
            "student":  student["name"],
            "roll_no":  student["roll_no"],
            "subjects": marks_list,
            "total":    total,
            "average":  average,
            "grade":    grade
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        cursor.close()
        conn.close()


# ─────────────────────────────────────────────
# 7. FIND TOPPER
# GET /students/topper
# Returns student with highest average marks
# ─────────────────────────────────────────────
@app.route("/students/topper", methods=["GET"])
def find_topper():
    try:
        conn   = get_connection()
        cursor = conn.cursor(dictionary=True)

        sql = """
            SELECT
                s.id,
                s.name,
                s.roll_no,
                s.department,
                ROUND(AVG(m.marks), 2) AS average_marks
            FROM students s
            JOIN marks m ON s.id = m.student_id
            GROUP BY s.id, s.name, s.roll_no, s.department
            ORDER BY average_marks DESC
            LIMIT 1
        """
        cursor.execute(sql)
        topper = cursor.fetchone()

        if not topper:
            return jsonify({"error": "No marks data available"}), 404

        topper["grade"] = calculate_grade(topper["average_marks"])

        return jsonify({
            "message": "Topper found!",
            "topper":  topper
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        cursor.close()
        conn.close()


# ─────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True, port=5000)
