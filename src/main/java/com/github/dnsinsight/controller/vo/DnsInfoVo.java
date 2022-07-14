package com.github.dnsinsight.controller.vo;

import lombok.Builder;
import lombok.Data;
import lombok.experimental.Accessors;

import java.io.Serializable;
import java.util.List;

/**
 * @Author: Tachikoma
 * @Date: 2022-07-02 22:54
 * @Description:
 */
@Data
@Builder
@Accessors(chain = true)
public class DnsInfoVo implements Serializable {
    private static final long serialVersionUID = 1L;

    private List<String> aa;
    private List<String> aaaa;
    private List<String> ns;
    private List<String> mx;
    private List<String> cname;
    private List<String> ptr;
}
