# IFNULL: 해당 column의 값이 null을 반환할 때, 다른 값으로 출력할 수 있도록 하는 함수
# SELECT IFNULL(Column명, "Null일 경우 대체 값") FROM 테이블명;

SELECT PT_NAME,PT_NO,GEND_CD,AGE, IFNULL(TLNO,'NONE')
FROM PATIENT
WHERE AGE<=12 AND GEND_CD="W"
ORDER BY AGE DESC, PT_NAME ASC