SELECT
    a.id,
    a.name,
    a.status,
    a.breed,
    a.customer_id,
    a.location_id,
    l.name location_name,
    l.address location_address
FROM Animal a
JOIN Location l
    ON l.id = a.location_id